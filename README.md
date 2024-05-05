# wger

<img src="https://raw.githubusercontent.com/wger-project/wger/master/wger/core/static/images/logos/logo.png" width="100" height="100"  alt="wger logo"/>

wger (ˈvɛɡɐ) Workout Manager is a free, open source web application that helps
you manage your personal workouts, weight and diet plans and can also be used
as a simple gym management utility. It offers a REST API as well, for easy
integration with other projects and tools.

For a live system, refer to the project's site: <https://wger.de/>

<img
src="https://raw.githubusercontent.com/wger-project/wger/master/wger/software/static/images/screens-3.png"
alt="Screenshot"
width="400">

## Mobile app

[<img src="https://play.google.com/intl/en_us/badges/images/generic/en-play-badge.png"
alt="Get it on Google Play"
height="80">](https://play.google.com/store/apps/details?id=de.wger.flutter)
[<img src="https://fdroid.gitlab.io/artwork/badge/get-it-on.png"
alt="Get it on F-Droid"
height="80">](https://f-droid.org/packages/de.wger.flutter/)

## Installation

These are the basic steps to install and run the application locally on a Linux
system. There are more detailed instructions, other deployment options as well
as an administration guide available at <https://wger.readthedocs.io> or in the
[docs repo](https://github.com/wger-project/docs).

Please consult the commands' help for further information and available
parameters.

### Production

If you want to host your own instance, take a look at the provided docker
compose file. This config will persist your database and uploaded images:

<https://github.com/wger-project/docker>

### Demo

If you just want to try it out:

```shell script
    docker run -ti --name wger.demo --publish 8000:80 wger/demo
```

Then just open <http://localhost:8000> and log in as **admin**, password **adminadmin**

Please note that this image will overwrite your data when you pull a new version,
it is only intended as an easy to setup demo

### Development version

We provide a docker file that sets everything up for development (however this won't
persist any data)

````shell script
docker run -ti  \
    -v /path/to/your/wger/checkout:/home/wger/src \
    --name wger.dev \
    --publish 8000:8000 \ 
    wger/server
````

Then just open <http://localhost:8000> and log in as: **admin**, password **adminadmin**

For more info, check the [README in wger/extras/developemt](
./extras/docker/development/README.md
).

Alternatively you can use the production compose file for development as well,
just bind your local source code into the web container (see the docker-compose.yml
file for details). You will also probably want to set `DJANGO_DEBUG to false

#### Local installation

If you prefer a local installation, consult the
[development documentation](https://wger.readthedocs.io/en/latest/development.html)

## Instructions for Use

### Create New Nutrition Plan

1. Select “Nutrition” on the top app bar, and click on “Nutrition Plans”.
2. Select the floating addition icon on the bottom right of the screen.
3. The pop-up screen allows you to name your nutrition plan,
   along with selecting two options.
  * Option one: Toggles calorie-only mode in the nutrition log. When deselected,
    the user can assign ingredients into planned “meals” for ease of logging.
    Otherwise, all logs are assigned by individual ingredients
  * Option two: Toggles macronutrient goals. The user will enter consumption goals for protein,
    carbohydrates and fats along with overall calories.

Once in the nutrition plan, there are two sections. The top section is where diary entries
and meals are created, along with estimated macronutrient totals. The lower section shows
what macronutrients have already been logged, along with a graph of macronutrient totals
and averages in the past week.

#### Add Diary Entry

1. To add a diary entry, click on the writing icon in the “Other logs” card.
   Hovering over it will say “Add nutrition diary entry”.
2. Once opened, the user can search for food or ingredients and enter the tracked
   unit value for the food. The date and time will can be set for previous entries
   if needed. Once finished, press “Submit” and the macronutrient totals will
   appear on the “Logged” section of the screen.

#### Create Meal

1. To add a meal, the user will click on the plus sign underneath the “Other logs” card
   to open up two entry boxes for a meal name and time. Clicking “Submit” will add that
   meal to a new card above the “Other logs” card.
2. To add food to a meal, the user will click on the plus sign in the meal card, where the user can
   search for food and enter the amount of food in the meal then “Submit” to add to the meal card.
   This can be for as many times as needed to finish the ingredients of the meal.
3. Once the food has been added to the meal, the meal can be added in whole to the nutrition log
   by clicking the writing icon in the top right of the meal card.

Both cards can be extended to give more detail about what has been logged from each.
Meal cards will show how much of the day’s total has come from the meal.

## Contact

Feel free to contact us if you found this useful or if there was something that
didn't behave as you expected. We can't fix what we don't know about, so please
report liberally. If you're not sure if something is a bug or not, feel free to
file a bug anyway.

* **Discord:** <https://discord.gg/rPWFv6W>
* **Issue tracker:** <https://github.com/wger-project/wger/issues>
* **Mastodon:** <https://fosstodon.org/@wger>

## Sources

All the code and the content is available on github:

<https://github.com/wger-project/wger>

## Translation

Translate the app to your language on [Weblate](https://hosted.weblate.org/engage/wger/).

[![translation status](https://hosted.weblate.org/widgets/wger/-/multi-blue.svg)](https://hosted.weblate.org/engage/wger/)

## License

The application is licensed under the Affero GNU General Public License 3 or
later (AGPL 3+).

The initial exercise and ingredient data is licensed additionally under one of
the Creative Commons licenses, see the individual exercises for more details.

The documentation is released under a CC-BY-SA: either version 4 of the License,
or (at your option) any later version.

Some images were taken from Wikipedia, see the SOURCES file in their respective
folders for more details.
