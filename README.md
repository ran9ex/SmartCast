��#   S m a r t C a s t

<br>

 
 
<h1 align="center" style="color:#4931AF;">SmartCastApp</h1>

## Project Idea

Our idea is to develop a live football streaming application powered by artificial intelligence to enhance the viewing experience for all segments of society. The app offers instant commentary and smart match analysis, which can be customized to be simplified or detailed based on user preference. It aims to make football more accessible, even for those without prior knowledge of the game.

### Accessibility Features

The application is also designed to provide a personalized experience for individuals with special needs, including:
- Audio commentary for the visually impaired.
- Visual written analysis for those with hearing impairments.
- Colorblind-friendly display, where teams are visually distinguished using appropriate color filters. Users can upload a .mp4 video, and the system will adjust the visuals accordingly.

### Datasets and Models

To achieve this, we used open datasets from [Roboflow](https://roboflow.com/) and trained two models using YOLOv8:
- Player Detector Model, located in the train_model_for_player_detector/ directory.
- Football Event Detection Model, located in the footballevent/ directory.

These models are used in our code to detect players and events from uploaded match videos.

### Note

- The system requires uploading a video file in .mp4 format to function properly.

<br>
### Datasets Used

<table style="background-color:#f0edfb; border: 1px solid #ddd; border-radius: 8px;" align="center">
  <tr>
    <th style="color:#4931AF;">Dataset Name</th>
    <th style="color:#4931AF;">Link</th>
  </tr>
  <tr>
    <td>Football Goalpost</td>
    <td><a href="https://universe.roboflow.com/inplayin/football-goalpost">Roboflow Dataset</a></td>
  </tr>
  <tr>
    <td>Football Players Detection</td>
    <td><a href="https://universe.roboflow.com/saraj/football-players-detection-3zvbc-bu2wx">Roboflow Dataset</a></td>
  </tr>
  <tr>
    <td>Football Events</td>
    <td><a href="https://universe.roboflow.com/navin-rv0wp/football_events">Roboflow Dataset</a></td>
  </tr>
</table>





