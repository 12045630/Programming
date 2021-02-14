using System;

namespace Snake
{
    partial class Snake
    {
        class Music
        {
			public Music()
            {

            }
				
			public void MainMusic()
            {
				var mainMusic = MediaPlayer();
				string uri = "@";
				mainMusic.Open(new Uri(uri, UriKind, Relative));
				mainMusic.Volume = 15;
				mainMusic.Play();
            }
        }
	}
}