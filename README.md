# Autoclicker

Here is my autoclicker GUI that I worked on across the span of my February half term. I'm utilising PySide6 to help myself when I come to do my non-exam assessment in my Computer Science A-level course.
I've never worked with an application that interacts with my OS in a way that PyAutoGui does, so it was a valuable and informative experience that I can keep with me when it comes to tackling other programming tasks in the future.

# Usage
My application has an easy to navigate GUI and a fairly basic setup. You can set a specific amount of clicks to be carried out, or you can set the spinbox's value to `-1` for an infinite amount of clicks until the failsafe is triggered. You are also 
able to customise at what pace the application will carry out these clicks, this is measured in *clicks per second*. The autoclicker will begin once you press `Start autoclicker` or when the hotkey `f4` is pressed. The failsafe built into PyAutoGui can be triggered 
by slamming your mouses cursor into one of the four corners of your monitor, causing it to exit early.