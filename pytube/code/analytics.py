from datetime import date
from math import ceil
import matplotlib.pyplot as plt
from matplotlib.pyplot import Figure
import pandas as pd
from pandas import DataFrame


class Analytics:

    def __init__(self, name: str):
        self.name = name

    def _heatmap(self, df: DataFrame) -> DataFrame:
        return (
            df 
            .style.background_gradient(cmap ='YlOrRd', axis=None)
            .set_properties(**{'font-size': '20px'})
        )

    def read(self) -> None:
        df = pd.read_csv(f"./data/{self.name}.csv")
        df["publish_date"] = df.publish_date.apply(lambda s: date.fromisoformat(s))
        df["year"] = df.publish_date.apply(lambda d: d.year)
        df["month"] = df.publish_date.apply(lambda d: d.month) 
        df["minutes"] = df.length / 60

        self.data = df

    def get_videos_per_month(self, heatmap: bool = False) -> DataFrame:

        videos_per_month = (
            self.data
            .groupby(["year", "month"]).size()
            .reset_index()
            .rename({0: "tot"}, axis=1)
            .pivot(values="tot", columns="month", index="year")
            .fillna(0)
        )

        for c in videos_per_month.columns:
            videos_per_month = videos_per_month.astype({c: int})
            
        videos_per_month["tot"] = videos_per_month.apply(lambda r: sum(r), axis=1)
        videos_per_month["mean"] = videos_per_month.tot.apply(lambda n: int(round(n / 12)))

        if heatmap is True:

            videos_per_month = self._heatmap(videos_per_month[list(range(1, 13))])

        return videos_per_month

    def get_videos_per_year(self) -> Figure:

        videos_per_year = self.data.groupby("year").size().reset_index().rename({0: "tot"}, axis=1)

        fig = plt.figure(figsize=(10, 5))

        plt.bar(videos_per_year.year, videos_per_year.tot)

        for x, y in zip(videos_per_year.year, videos_per_year.tot):
            plt.text(x, y, y, ha = 'center')
            
        plt.tick_params(left=False, labelleft = False)
        plt.title("#VIDEOS")

        plt.close()

        return fig 
        
    def get_views_from_month(
        self, 
        weight: int = 6, 
        videos_info: bool = False,
        heatmap: bool = False
    ) -> DataFrame:

        views_from_month = (

            self.data
            .groupby(["year", "month"]).sum("views")
            .reset_index()
            .pivot(values="views", columns="month", index="year")
            .fillna(0)
        )

        views_from_month["tot"] = views_from_month.apply(lambda r: sum(r), axis=1)
        views_from_month["mean"] = round(views_from_month.tot / 12)
            
        views_from_month = views_from_month / (10 ** weight)

        for c in views_from_month.columns:
            views_from_month = views_from_month.astype({c: int})

        if videos_info is True:
            
            videos_per_month = self.get_videos_per_month()

            views_from_month["n_videos"] = videos_per_month["tot"]
            views_from_month["per_video"] = views_from_month.apply(lambda r: int(r.tot / r.n_videos), axis=1)
    
        if heatmap is True:
            views_from_month = self._heatmap(views_from_month[list(range(1, 13))])
    
        return views_from_month 

    def get_avg_views_from_month(self, weight: int = 6, heatmap: bool = False) -> DataFrame:

        avg_views_from_month = (
            self.data 
            .groupby(["year", "month"]).size()
            .reset_index()
            .rename({0: "tot"}, axis=1)

            .merge(
                
                self.data 
                .groupby(["year", "month"]).sum("views")
                .reset_index(),
            
                on=["year", "month"]
            )
        )

        avg_views_from_month["mean"] = avg_views_from_month.apply(lambda r: int(r.views / r.tot / (10 ** weight)), axis=1)

        avg_views_from_month = avg_views_from_month.pivot(values="mean", columns="month", index="year").fillna(0)

        for c in avg_views_from_month.columns:
            avg_views_from_month = avg_views_from_month.astype({c: int})
            
        if heatmap is True:
            avg_views_from_month = self._heatmap(avg_views_from_month) 

        return avg_views_from_month

    def get_total_minutes_per_month(self, heatmap: bool = True) -> DataFrame:

        minutes_per_month = (
    
            self.data 
            .groupby(["year", "month"]).sum("minutes")
            .reset_index()
            .pivot(values="minutes", columns="month", index="year")
            .fillna(0)
            
        )

        for c in minutes_per_month.columns:
            minutes_per_month = minutes_per_month.astype({c: int})
            
        if heatmap is True:
            minutes_per_month = self._heatmap(minutes_per_month)

        return minutes_per_month

    def get_avg_minutes_per_month(self, heatmap: bool = False) -> DataFrame:
   
        minutes_per_month = (

            self.data 
            .groupby(["year", "month"]).size()
            .reset_index()
            .rename({0: "tot"}, axis=1)
            
            .merge(

                self.data 
                .groupby(["year", "month"]).sum("minutes")
                .reset_index(),
                on=["year", "month"]
            
            )
        )

        minutes_per_month["mean"] = minutes_per_month.apply(lambda r: int(r.minutes / r.tot), axis=1)

        minutes_per_month = minutes_per_month.pivot(values="mean", columns="month", index="year").fillna(0)

        for c in minutes_per_month.columns:
            
            minutes_per_month = minutes_per_month.astype({c: int})
            
        minutes_per_month["tot"] = minutes_per_month.apply(lambda r: sum(r), axis=1)
        minutes_per_month["mean"] = minutes_per_month.tot.apply(lambda n: int(round(n / 12)))

        if heatmap is True:
            minutes_per_month = self._heatmap(minutes_per_month)

        return minutes_per_month
