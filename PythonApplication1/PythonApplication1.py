#! /usr/bin/env python

from __future__ import print_function
import rospy
import actionlib
from om_aiv_navigation.msg import ActionAction, ActionGoal, ActionResult
from sound_play.msg import SoundRequest
from sound_play.libsoundplay import SoundClient

def goto_client(desired_goal, sound_client):
    # Creates the SimpleActionClient, passing the type of the action
    # (FibonacciAction) to the constructor.
    client = actionlib.SimpleActionClient('action_servers', ActionAction)

    # Waits until the action server has started up and started
    # listening for goals.
    client.wait_for_server()

    # Creates a goal to send to the action server.
    goal = ActionGoal("goto " + desired_goal, ["Arrived at " + desired_goal])

    # Sends the goal to the action server.
    client.send_goal(goal)

    # Waits for the server to finish performing the action.
    client.wait_for_result()

    # Prints out the result of executing the action
    result = client.get_result()

    return result

def play_audio(file_path, sound_client):
    # Plays the audio file
    sound_handle = sound_client.playWave(file_path)
    
    # Waits for the audio to finish playing
    rospy.sleep(sound_handle.getDuration())

if __name__ == '__main__':
    try:
        # Initializes a rospy node so that the SimpleActionClient can
        # publish and subscribe over ROS.
        rospy.init_node('goto_goal2_action_py')

        # Initialize SoundClient for playing audio
        sound_client = SoundClient()

        # First goal
        result = goto_client("Goal2", sound_client)
        play_audio("/path/to/your/audio/file1.mp3", sound_client)  # Replace with the actual audio path were going to use

        # Second goal
        result = goto_client("Goal3", sound_client)
        play_audio("/path/to/your/audio/file2.mp3", sound_client)  # Replace with the actual audio path were going to use

        print("Result:", result)
    except rospy.ROSInterruptException:
        print("program interrupted before completion", file=sys.stderr)
