# srt-repairer

*Repair srt files that mpv can't recognize*

Sometimes there are srt files start with "0" in the first line. Mpv can't load this  kind of format.

The main function of this script is to remove the unwanted "0"s in all srt files and also the tailer index of every line of captions.

## Repair example
<pre>
<del>0</del>
1
00:00:01,330 --> 00:00:05,330
xx, xxxx xx xxxxx xxx xxxxx xxx xxxxxx.
<del>1</del>

2
00:00:05,330 --> 00:00:10,330
xxx xxxxx x xxxx xx xxxx xxx x xxxxxx xxx xxxxx xx, xxxxxxx xxxx xx xxxx xxxx x
<del>2</del>

3
00:00:10,330 --> 00:00:15,330
xxxxxx. xx'x x xxxxxxx. xxx xx'x x xxxxxxxxx.
<del>3</del>
</pre>

## How to use it

Change the source pathname and the target folder name in the main.py. Then run it. The cooked srt files will appear in the target folder under current directory.

```python
# 👇 Change code here 👇
source_pathname = r"X:\Xxxx\Xxxxx\**\*.srt"
target_folder_name = "srts"
# 👆 Change code here 👆
```

```console
PS C:\Users\xxx\xxx\srt-repairer> python main.py
```