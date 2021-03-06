﻿using WMPLib;
namespace Snake
{
    public class Sounds
    {
        WindowsMediaPlayer player = new WindowsMediaPlayer();
        private string pathToMedia;

        public Sounds(string pathToResources)
        {
            pathToMedia = pathToResources;
        }

        public void Play()
        {
            player.URL = pathToMedia + "main.mp3";
            player.settings.volume = 3;
            player.controls.play();
            player.settings.setMode("loop", true);
        }

        public void EatPlay()
        {
            player.URL = pathToMedia + "eat.mp3";
            player.settings.volume = 50;
            player.controls.play();
        }

        public void PlaySpsEat()
        {
            player.URL = pathToMedia + "good.mp3";
            player.settings.volume = 50;
            player.controls.play();
        }
        public void PlayBadEat()
        {
            player.URL = pathToMedia + "bad.mp3";
            player.settings.volume = 50;
            player.controls.play();
        }
        public void PlayStop()
        {
            player.URL = pathToMedia + "main.mp3";
            player.controls.stop();
        }
    }
}


