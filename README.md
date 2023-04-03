# AI5A/misc

Misc scripts that I have written and find useful for ham radio endeavors.

## License

MIT except where noted in individual files.

## What exists?

#### `turkeyalert`

This is a simple script to connect to the hamalert.org telnet cluster emulation
server and use the Linux `notify-send` command to trigger desktop notifications
for interesting spots. Any alerts that you send to "telnet" on hamalert.org
will get displayed. You can run this on-login and/or as a systemd user service.

You must set `HAMALERT_USERNAME` and `HAMALERT_PASSWORD` environment variables
before using this script.

---

#### `ham-radio-prefixes.apkg`

This is an Anki deck I've generated for learning callsign prefixes for various
countries/entities. Ultimately this comes from the ARRL DXCC list (without
deleted entities), but prefixes that had more than one line in the list have
been merged into one note/card (otherwise it would be impossible to know which
one was being asked).

---

#### `my-qrz-page.html`

qrz.com does some (easily bypassed) things to try to limit what can be done on
one's profile page.

I do some interesting things on my page to clean it up, namely I use a CSS-only
implementation of tabs originally based on
[this codepen](https://codepen.io/MPDoctor/pen/mpJdYe).

However because of the things I do to make this work, you cannot "re-save" the
bio page once it is saved. Their horrible editor will remove important
attributes and break the page. So, you have to paste (in source view in their
editor) the entire page each time you want to edit it.
