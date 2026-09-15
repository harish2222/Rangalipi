### Name

Rangalipi

### Description

Rangalipi: Kanagawa dark glass islands, gold borders, palette and font switchers.

### Homepage

https://github.com/harish2222/Rangalipi

### Image

PREVIEW_PNG_URL

### Theme Styles

```css
/* Rangalipi for YASB - Kanagawa dark islands, gold borders, liquid glass */
@import "yasb_colors.css";

/* Root Variables */
:root {

      --icons-font: "Mononoki Nerd Font Propo";
      --icons-font-fallback: "Mononoki Nerd Font Propo";
      --system-font: "Mononoki Nerd Font Propo";
      --specialFont: "Mononoki Nerd Font Propo";
    --border-radius: 14;
    --border-radius2: 4;
    --border-radius3: 10;
    --border-radiusWallpapers: 10;
    --fontSize: 12px;
    --iconSize: 16px;
    --fontSizeLarge: 16px;
    --fontWeight: 600;

    /*colors*/

    --background: #1F1F28;
    --background2: #2A2A37;
    --accent: #C8C093;
    --text: #DCD7BA;
    --accentText: #1F1F28;
    --hover: #363646;
    --mutedBG: #090618;
    --border: #E6C384;
    --redFlash: #C34043;
    --subtext: #C8C093;
    --base: #1F1F28;
    --mantle: #16161D;
    --crust: #090618;
    --surface0: #2A2A37;
    --surface1: #363646;
    --surface2: #54546D;
    --overlay0: #727169;
    --overlay1: #938AA9;
    --overlay2: #9CABCA;
    --subtext0: #938AA9;
    --subtext1: #C8C093;
    --lavender: #9CABCA;
    --blue: #7E9CD8;
    --sapphire: #7FB4CA;
    --sky: #A3D4D5;
    --teal: #7AA89F;
    --green: #98BB6C;
    --yellow: #E6C384;
    --peach: #FFA066;
    --maroon: #E46876;
    --red: #C34043;
    --mauve: #957FB8;
    --pink: #D27E99;
    --flamingo: #E8C8C8;
    --rosewater: #DCD7BA;
    --text-muted: #C8C093;
    --yasb-icon-fg: #DCD7BA;
    --glass: rgba(31, 31, 40, 0.8);
}

/* Global Defaults */
* {
    font-size: var(--fontSize);
    font-weight: var(--fontWeight);
    font-family: var(--system-font);
    color: var(--text);
}


/* Bar - islands, Glazing Mocha glass */
.yasb-bar {
    background-color: transparent;
    border: none;
    padding: 0 4px;
}
.yasb-bar.adaptive {
    background-color: var(--glass);
    border: none;
    -qproperty-railheight: 0;
    -qproperty-islandradius: 12;
    -qproperty-grouppadding: 8;
    -qproperty-islands: true;
    -qproperty-edgeradius: 0;
    -qproperty-borderwidth: 1;
    -qproperty-bordercolor: var(--border);
}
.container-left,
.container-center,
.container-right {
    background-color: transparent;
    padding: 0 8px;
    margin: 0;
}

/* Tooltip */
.tooltip {
    background-color: var(--background);
    border-radius: var(--border-radius);
    color: var(--text);
    padding: 5px 10px;
    font-size: var(--fontSize);
    font-family: var(--system-font);
    font-weight: var(--fontWeight);
    margin-top: 4px;
    border: 1px solid var(--border);
}

/* Context Menu */
.context-menu,
.context-menu .menu-checkbox {
    background-color: var(--background);
    border-bottom: 1px solid var(--border);
    padding: 4px 0px;
    font-family: var(--system-font);
    font-weight: var(--fontWeight);
    font-size: var(--fontSize);
    color: var(--text);
}
.context-menu {
    border-radius: var(--border-radius);
    border: 1px solid var(--border);
}
.context-menu::right-arrow {
    width: 8px;
    height: 8px;
    padding-right: 24px;
}
.context-menu::item,
.context-menu .menu-checkbox {
    background-color: transparent;
    padding: 6px 12px;
    margin: 2px 6px;
    border-radius: var(--border-radius);
    min-width: 100px;
}
.context-menu::item:selected,
.context-menu .menu-checkbox:hover {
    background-color: var(--hover);
    color: var(--text);
    border-radius: var(--border-radius3);
}
.context-menu::separator {
    height: 1px;
    background-color: var(--background2);
    margin: 4px 8px;
}
.context-menu::item:disabled {
    color: var(--overlay0);
    background-color: transparent;
}
.context-menu .menu-checkbox .checkbox {
    border: none;
    padding: 8px 16px;
    font-size: var(--fontSize);
    margin: 0;
    color: var(--text);
    font-family: var(--system-font);
    font-weight: var(--fontWeight);
}
.context-menu .submenu::item:disabled {
    margin: 0;
    padding-left: 16px;
}
.context-menu .menu-checkbox .checkbox:unchecked {
    color: var(--text);
}
.context-menu .menu-checkbox .checkbox::indicator {
    width: 12px;
    height: 12px;
    margin-left: 0px;
    margin-right: 8px;
}
.context-menu .menu-checkbox .checkbox::indicator:unchecked {
    background: var(--mutedBG);
    border-radius: 2px;
}
.context-menu .menu-checkbox .checkbox::indicator:checked {
    background: var(--accent);
    border-radius: 2px;
}
.context-menu .menu-checkbox .checkbox:focus {
    outline: none;
}

/* Base Widget Styles - plain strip */
.widget {
    padding-left: 6px;
    padding-right: 6px;
    margin: 0 2px;
    background-color: transparent;
    border-radius: 0;
    border: none;
}

.widget .icon {
    font-size: var(--iconSize);
    font-weight: var(--fontWeight);
    color: var(--yasb-icon-fg);
    font-family: var(--icons-font-fallback);
}

.widget .label {
    color: var(--text);
    font-weight: var(--fontWeight);
    padding-bottom: 2px;
}

/* Home Menu */
.home-widget .icon {
    font-family: var(--system-font);
    font-size: 18px;
    font-weight: bold;
    color: var(--lavender);
    padding-bottom: 0.5px;
}

.home-menu {
    background-color: var(--glass);
    border: 1px solid var(--border);
    border-radius: var(--border-radius);
    margin-top: 3px;
}
.home-menu .menu-item {
    color: var(--text);
    padding: 10px 48px 10px 16px;
    font-family: var(--system-font);
    font-weight: var(--fontWeight);
    margin-top: 3px;
}
.home-menu .menu-item:hover {
    background-color: var(--hover);
    color: var(--text);
    border-radius: var(--border-radius3);
    margin-left: 4px;
    margin-right: 4px;
    margin-top: 7px;
    margin-bottom: 4px;
}
.home-menu .separator {
    max-height: 0px;
    background-color: var(--background2);
}

/* Clock */

.clock-widget .widget-container {
    background-color: transparent;
    border: none;
    border-radius: 0;
    margin: 1px 1px;
    padding: 2 4px;
}

.clock-widget .label {
    color: var(--text);
    margin: 0 2px;
}

.clock-widget {
    padding: 2 2px;
}

.clock-widget .icon.alarm {
    color: var(--text);
    padding-left: 4px;
    padding-right: 4px;
}
.clock-popup.alarm,
.clock-popup.timer,
.clock-popup.calendar {
    min-width: 460px;
    background-color: var(--background);
    border-radius: var(--border-radius);
    border: 1px solid var(--border);
}
.clock-popup.calendar .calendar-table,
.clock-popup.calendar .calendar-table::item {
    background-color: var(--background);
    color: var(--text);
    font-family: var(--system-font);
    margin: 0;
    padding: 0;
    border: none;
    outline: none;
}
.clock-popup.calendar .calendar-table::item:selected {
    color: var(--accentText);
    font-weight: bold;
    background-color: var(--accent);
    border-radius: 12px;
}
.clock-popup.calendar .day-label {
    margin-top: 20px;
}
.clock-popup.calendar .day-label,
.clock-popup.calendar .month-label,
.clock-popup.calendar .year-label,
.clock-popup.calendar .date-label {
    font-family: var(--system-font);
    font-size: var(--iconSize);
    font-weight: 700;
    min-width: 180px;
    max-width: 180px;
}
.clock-popup.calendar .month-label {
    font-weight: normal;
}
.clock-popup.calendar .year-label {
    font-weight: normal;
}
.clock-popup.calendar .date-label {
    font-size: 88px;
    font-weight: 900;
    margin-top: -20px;
}
.clock-popup.timer .clock-popup-container,
.clock-popup.alarm .clock-popup-container {
    padding: 16px;
    background-color: var(--background);
    border-radius: var(--border-radius);
}
.clock-popup.timer .clock-popup-footer,
.clock-popup.alarm .clock-popup-footer {
    padding: 16px;
    background-color: var(--background2);
    border-radius: var(--border-radius);
}
.clock-popup .clock-label-timer {
    font-size: 13px;
    font-family: var(--system-font);
    font-weight: var(--fontWeight);
}
.clock-popup .clock-input-time {
    font-size: 48px;
    background-color: var(--background);
    border: none;
    font-family: var(--system-font);
    font-weight: var(--fontWeight);
}
.clock-popup .clock-input-time.colon {
    padding-bottom: 8px;
}
.clock-popup .button {
    border-radius: 4px;
    font-family: var(--system-font);
    font-weight: var(--fontWeight);
    font-size: 13px;
    min-height: 28px;
    min-width: 64px;
    margin: 4px 0;
    background-color: var(--background2);
}
.clock-popup .button.save,
.clock-popup .button.start,
.clock-popup .button.delete,
.clock-popup .button.cancel {
    min-width: 120px;
}
.clock-popup .button.save,
.clock-popup .button.start {
    background-color: var(--background2);
    color: var(--text);
    margin-right: 8px;
}
.clock-popup .button.save:hover,
.clock-popup .button.start:hover {
    background-color: var(--background2)
}
.clock-popup .button.is-alarm-enabled {
    background-color: var(--background);
}
.clock-popup .button.is-alarm-enabled:hover {
    background-color: var(--background);
}
.clock-popup .button.is-alarm-disabled {
    background-color: var(--background);
}
.clock-popup .button.day {
    background-color: var(--background2);
    max-height: 20px;
    min-height: 20px;
}
.clock-popup .button.day:checked {
    background-color: var(--accent);
    color: var(--accentText);
}
.clock-popup .button.quick-option {
    background-color: var(--background2);
}
.clock-popup .button.quick-option:checked {
    background-color: var(--accent);
    color: var(--accentText);
}
.clock-popup .button:hover {
    background-color: var(--hover);
}
.clock-popup .button:disabled {
    background-color: var(--background2);
    color: var(--text);
}
.clock-popup .alarm-input-title {
    font-size: 14px;
    font-family: var(--system-font);
    font-weight: var(--fontWeight);
    color: var(--text-muted);
    background-color: var(--background2);
    border: 1px solid transparent;
    border-radius: 4px;
    padding: 4px 8px;
    margin-top: 8px;
    outline: none;
    min-width: 300px;
}
.clock-popup .alarm-input-title:focus {
    border: 1px solid var(--accent);
}
.active-alarm-window {
    background-color: var(--background);
    max-width: 500px;
    min-width: 500px;
    padding: 32px;
    border-radius: var(--border-radius);
}
.active-alarm-window .alarm-title-icon {
    font-size: 88px;
    color: var(--text);
    margin-bottom: 16px;
}
.active-alarm-window .alarm-title {
    font-size: 24px;
    font-family: var(--system-font);
    font-weight: var(--fontWeight);
    color: var(--text);
    max-width: 500px;
    min-width: 500px;
}
.active-alarm-window .alarm-info {
    font-size: var(--iconSize);
    font-family: var(--system-font);
    font-weight: var(--fontWeight);
    color: var(--text);
    margin-bottom: 32px;
}
.active-alarm-window .button {
    border-radius: 4px;
    font-family: var(--system-font);
    font-weight: var(--fontWeight);
    font-size: 13px;
    min-height: 36px;
    min-width: 100px;
    margin: 0 4px;
    background-color: var(--background2);
}
.active-alarm-window .button:hover {
    background-color: var(--hover);
}

/* Power Menu */

.power-menu-compact {
    min-width: 260px;
    background-color: var(--background);
    border-radius: var(--border-radius);
    margin-right: 14px;
    border: 1px solid var(--border);
}
.power-menu-compact .profile-info {
    padding: 24px 14 24px 0;
}
.power-menu-compact .profile-info .profile-username {
    font-size: var(--iconSize);
    font-weight: var(--fontWeight);
    color: var(--text);
    font-family: var(--system-font);
    margin-top: 4px;
}

.power-menu-widget .icon {
    color: var(--text);
}


.power-menu-compact .profile-info .profile-account-type {
    font-size: var(--fontSize);
    color: var(--accentText);
    font-weight: var(--fontWeight);
    margin-top: 8px;
    font-family: var(--system-font);
    background-color: var(--accent);
    padding: 2px 6px 3px 6px;
    border-radius: var(--border-radius2);
}

.power-menu-compact .profile-info .profile-email {
    font-size: var(--fontSize);
    color: transparent;
    margin-top: -10px;
    font-family: var(--system-font);
}

.power-menu-compact .manage-accounts {
    font-size: var(--fontSize);
    background-color: var(--background2);
    font-family: var(--system-font);
    font-weight: var(--fontWeight);
    padding: 3px 12px 4px 12px;
    color: var(--text);
    margin-top: 0px;
    border-radius: 4px;
    border: 0px solid var(--border);
}

.power-menu-compact .manage-accounts:hover {
    background-color: var(--accent);
    color: var(--accentText);
}

.power-menu-compact .buttons {
    margin: 0 26px 12px 12px;
    border-radius: var(--border-radius);
    background-color: transparent;
    border: none;
}
.power-menu-compact .button {
    padding: 8px 16px;
    margin: 2px;
    background-color: var(--background2);
    /* border: 1px solid var(--border); */
    color: var(--background2);
    border-radius: var(--border-radius2);
}
.power-menu-compact .button.hover {
    background-color: var(--accent);
}

.power-menu-compact .button .icon {
    font-size: var(--iconSize);
    font-weight: var(--fontWeight);
    color: var(--text);
    padding-right: 10px;
    min-width: 20px;
}
.power-menu-compact .button .label {
    font-size: 13px;
    font-weight: 500;
    font-family: var(--system-font);
    color: var(--text);
}
.power-menu-compact .icon.hover,
.power-menu-compact .label.hover {
    color: var(--accentText);
}

/* Volume */

.volume-widget .icon {
    color: var(--teal);
    font-family: var(--icons-font);
    padding-right: 5px;
}
.audio-menu {
    background-color: var(--glass); 
    border: 1px solid var(--border);
    min-width: 300px;
    border-radius: var(--border-radius);
}
/* System volume */
.audio-menu .system-volume-container .volume-slider {
    border: none;
}
/* Device list styles */
.audio-menu .audio-container .device {
    background-color:transparent;
    border: none;
    padding: 6px 12px;
    margin: 2px 6px;
    font-size: var(--fontSize);
    border-radius: var(--border-radius2);
}
.audio-menu .audio-container .device.selected {
    background-color: var(--background2);
    color: var(--text);
   
}
.audio-menu .audio-container .device:hover {
    background-color: var(--hover);
    color: var(--text);
}

.audio-menu .audio-container .device.selected:hover {
    background-color: var(--hover);
    color: var(--text);
}

/* Toggle button for application volumes (if is enabled) */
.audio-menu .toggle-apps {
    background-color: transparent;
    border: none;
    padding: 0;
    margin: 0;
    min-height: 24px;
    min-width: 24px;
    border-radius: 4px;
}
.audio-menu .toggle-apps.expanded {
    background-color: transparent;
}
.audio-menu .toggle-apps:hover {
    background-color: var(--hover);
    
}
/* Container for application volumes (if is enabled) */
.audio-menu .apps-container {
    padding: 8px;
    margin-top:10px;
    border-radius: var(--border-radius2);
    background-color: var(--background2);
}
.audio-menu .apps-container .app-volume .app-icon-container {
    min-width: 40px;
    min-height: 40px;
    max-width: 40px;
    max-height: 40px;
    border-radius: var(--border-radius);
    margin-right: 8px;
}
.audio-menu .apps-container .app-volume .app-icon-container:hover {
    background-color: var(--hover);
}

/* Active Windows Title */
.active-window-widget .icon {
    padding-right: 4px;
    padding-bottom: 0;
    color: var(--overlay1);
}


/* Separator_widget */
.separator-widget .widget-container .label{
    color: var(--overlay0);
    margin-left: -1px;
    margin-right: -1px;
}

/* Komorebi Workspaces */
/*Style for widget.*/
.komorebi-workspaces {
    padding: 0px 4px;
    border: 0px solid var(--border);
}

/*Style for widget container.*/
.komorebi-workspaces .widget-container {

}

/*Style for buttons.*/
.komorebi-workspaces .ws-btn {
    border: none;
    color: var(--overlay1);
}

/*Style for buttons which contain window and are not empty.*/
.komorebi-workspaces .ws-btn.populated {
    padding-left: 8;
    padding-right: 8;
    background-color: transparent;
    border-radius: var(--border-radius2);
    color: var(--subtext1);
} 

/*Style for the active workspace button.*/
.komorebi-workspaces .ws-btn.active {
    padding-left: 8;
    padding-right: 8;
    background-color: var(--background2);
    border-radius: var(--border-radius2);
    color: var(--accent);
    font-weight: 600;
    padding-top: 3px;
    padding-bottom: 3px;
} 


/* Komorebi-active-layout */
.komorebi-active-layout {}
.komorebi-active-layout .widget-container {}
.komorebi-active-layout .label {
    font-family: var(--specialFont);
    padding-top: 1px;
    color: var(--sapphire);
}

/* Komorebi-layout-menu */
.komorebi-layout-menu {
    background-color: var(--glass);
    border-radius: var(--border-radius);
    border: 1px solid var(--border);
}
.komorebi-layout-menu .menu-item {
    padding: 8px 16px;
    font-size: var(--fontSize);
    color: var(--text); 
    font-weight: var(--fontWeight);
    margin: 2px 2px;
}
.komorebi-layout-menu .menu-item-icon {
    color: var(--text);
    font-size: var(--iconSize);
}
.komorebi-layout-menu .menu-item-text {
    font-family: var(--system-font);
    padding-left:4px;
    font-size: var(--fontSize);
} 

.komorebi-layout-menu .menu-item:hover {
    background-color: var(--hover);
    border-radius: var(--border-radius3);
    margin: 4px 4px;
} 

.komorebi-layout-menu .separator {
    max-height: 1px;
    background-color: var(--background2);
}

/* Wallpapers-Widget */
.wallpapers-widget {
}

.wallpapers-widget .icon {
    color: var(--mauve);
}

.wallpapers-widget .widget-container {
}
.wallpapers-gallery-window {
    background-color: var(--background);
    margin: 16px;
    border-radius: var(--border-radius);
    border: 1px solid var(--border);
}
.wallpapers-gallery-image {
    border: 2px solid var(--border);
    border-radius: var(--border-radiusWallpapers);
}
.wallpapers-gallery-image:hover {
    border: 1px solid var(--accent);
}

/* Systray - Glazing Mocha semantic */
.systray {
    background: transparent;
    border: none;
}

/* Icon being dragged, we already apply some transparency to it so you don't need to use it */

.systray .pinned-container.drop-target {
    background: var(--background);
}
.systray .unpinned-visibility-btn {
    border-radius: 4px;
    height: 20px;
    width: 16px;
    border: none;
    outline: none;
}
.systray .label,
.systray .icon {
    color: var(--mauve);
}

.systray-popup {
    background-color: var(--glass);
    padding: 4px;
    border-radius: var(--border-radius);
    border: 1px solid var(--border);
}
.systray-popup .button {
    padding: 10px;
    margin: 0;
    border: 0;
    border-radius: 6px;
}
.systray-popup .button:hover {
    background-color: var(--hover);
    border-radius: var(--border-radius3);
}


/* notification-widget - Glazing Mocha semantic */
.notification-widget .icon {
    color: var(--overlay2);
}
.notification-widget .icon.new-notification {
    color: var(--blue);
}
.notification-widget .label.new-notification {
    color: var(--blue);
    font-weight: 600;
}

/* Media-Widget-Popup */

/* Media full features: bar controls, progress line, app volume */
.media-widget .btn {
    font-family: "Segoe Fluent Icons";
    font-size: 13px;
    font-weight: 400;
    color: var(--subtext);
    padding: 0 3px;
    margin: 0;
    background-color: transparent;
    border: none;
}
.media-widget .btn:hover {
    color: var(--text);
}
.media-widget .btn.play {
    font-size: 14px;
    color: var(--accent);
}
.media-widget .btn.disabled,
.media-widget .btn.disabled:hover {
    color: var(--overlay0);
    background-color: transparent;
}
.media-widget .progress-bar {
    max-height: 2px;
    background-color: transparent;
    border: none;
}
.media-widget .progress-bar::chunk {
    background-color: var(--accent);
    border-radius: 2px;
}
.media-menu .thumbnail {
    border-radius: 8px;
}
.media-menu .app-volume-container {
    background-color: var(--background2);
    padding: 8px 6px;
    border-radius: var(--border-radius2);
    margin-left: 10px;
}
.media-menu .app-volume-container .volume-slider::groove {
    background: var(--surface1);
    width: 2px;
    border-radius: 3px;
}
.media-menu .app-volume-container .volume-slider::sub-page {
    background: var(--accent);
    border-radius: 3px;
}
.media-menu .app-volume-container .volume-slider::handle {
    background: var(--accent);
    border-radius: 6px;
    height: 12px;
    width: 12px;
}
.media-menu .app-volume-container .mute-button,
.media-menu .app-volume-container .unmute-button {
    font-family: "Segoe Fluent Icons";
    font-size: 16px;
    color: var(--subtext);
    margin-top: 4px;
}
.media-menu .app-volume-container .unmute-button {
    color: var(--overlay0);
}
.media-menu {
    min-width: 440px;
    max-width: 440px;
    background-color: var(--glass);
    border: 1px solid var(--border);
    border-radius: var(--border-radius);
}
.media-menu .title,
.media-menu .artist,
.media-menu .source {
    font-size: 14px;
    font-weight: var(--fontWeight);
    margin-left: 10px;
    font-family: var(--system-font);
    color: var(--text);
}
.media-menu .artist {
    font-size: 13px;
    color: var(--subtext);
    margin-top: 0px;
}
.media-menu .source {
    font-size: 11px;
    color: var(--accentText);
    border-radius: 3px;
    background-color: var(--accent);
    padding: 2px 4px;
    font-weight: var(--fontWeight);
    font-family: var(--system-font);
    margin-top: 10px;
}

.media-menu .source.aimp {
    background-color: #6f42c1;
    color: #ffffff;
}
.media-menu .source.apple-music {
    background-color: #fa2b56;
    color: #ffffff;
}
.media-menu .source.brave {
    background-color: #fb542b;
    color: #ffffff;
}
.media-menu .source.chrome {
    background-color: #4285f4;
    color: #ffffff;
}
.media-menu .source.edge {
    background-color: #0078d4;
    color: #ffffff;
}
.media-menu .source.firefox {
    background-color: #ff7139;
    color: #ffffff;
}
.media-menu .source.foobar2000 {
    background-color: #444444;
    color: #ffffff;
}
.media-menu .source.media-player {
    background-color: #0078d4;
    color: #ffffff;
}
.media-menu .source.murglar {
    background-color: #8a8a8a;
    color: #ffffff;
}
.media-menu .source.musicbee {
    background-color: #ffcc00;
    color: #000000;
}
.media-menu .source.nsmusics {
    background-color: #e64a19;
    color: #ffffff;
}
.media-menu .source.opera {
    background-color: #ff1b2d;
    color: #ffffff;
}
.media-menu .source.qobuz {
    background-color: #003a6f;
    color: #ffffff;
}
.media-menu .source.spotify {
    background-color: #1db954;
    color: #ffffff;
}
.media-menu .source.tidal {
    background-color: #000000;
    color: #ffffff;
}
.media-menu .source.winamp {
    background-color: #f1a11b;
    color: #000000;
}
.media-menu .source.youtube {
    background-color: #ff0000;
    color: #ffffff;
}
.media-menu .source.youtube-music {
    background-color: #c51f1f;
    color: #ffffff;
}
.media-menu .source.zen {
    background-color: #2ecc71;
    color: #000000;
}
.media-menu .btn {
    font-family: var(--icons-font);
    font-size: 14px;
    font-weight: var(--fontWeight);
    margin: 10px 2px 0px 2px;
    min-width: 40px;
    max-width: 40px;
    min-height: 40px;
    max-height: 40px;
    border-radius: 20px;
    color: var(--accent);
    background-color: var(--background2);
}
.media-menu .btn.prev {
    margin-left: 10px;
    color: var(--accent);
}
.media-menu .btn:hover {
    color: var(--mutedBG);
    background-color: var(--accent);
}
.media-menu .btn.play {
    background-color: var(--accent);
    font-size: 20px;
    color: var(--accentText);
}
.media-menu .btn.disabled:hover {
    color: var(--accent);
    background-color: var(--background);
}

.media-menu .btn.disabled {
    background-color: transparent;
}

.media-menu .btn.play:hover {
    background-color: var(--text);
    color: var(--mutedBG);
}

.media-menu .playback-time {
    font-size: 13px;
    font-family: var(--system-font);
    color: var(--subtext);
    margin-top: 20px;
    min-width: 100px;
}
.media-menu .progress-slider {
    height: 10px;
    margin: 5px 4px;
    border-radius: 3px;
}
.media-menu .progress-slider::groove {
    background: transparent;
    height: 2px;
    border-radius: 3px;
    background: var(--background2);

}
.media-menu .progress-slider::groove:hover {
    background: transparent;
    height: 6px;
    border-radius: 3px;
    background: var(--background2);
}
.media-menu .progress-slider::sub-page {
    background: var(--accent);
    border-radius: 3px;
    height: 4px;
}

/* Language-Widget */
.language-menu {
    background-color: var(--glass);
    min-width: 300px;
    border: 1px solid var(--border);
    border-radius: var(--border-radius);
}
.language-menu .header {
    color: transparent;
    padding-bottom: -12px;
}
.language-menu .footer {
    color: transparent;
    padding-top: -12px;
}

.language-menu .language-item {
    padding: 6px 12px;
    margin: 2px 4px;
    border-radius: var(--border-radius2);
}
.language-menu .language-item.active {
    background-color: var(--background2);
    border-radius: 4px;
    color: var(--text);
    border-radius: var(--border-radius2);
}
.language-menu .language-item:hover {
    background-color: var(--hover);
    color: var(--text);
    border-radius: var(--border-radius2);
}
.language-menu .language-item.active:hover {
    background-color: var(--hover);
    border-radius: 4px;
    border-radius: var(--border-radius2);
}
.language-menu .language-item .code {
    font-weight: 900;
    font-size: 14px;
    min-width: 40px;
    text-transform: uppercase;
}
.language-menu .language-item .icon {
    font-size: var(--iconSize);
    margin-right: 8px;
    color: var(--text);
}
.language-menu .language-item .name {
    font-weight: var(--fontWeight);
    font-family: var(--system-font);
    font-size: 14px;
}
.language-menu .language-item .layout {
    font-weight: var(--fontWeight);
    font-family: var(--system-font);
    font-size: var(--fontSize);
}

/* Launcher */
/* Quick Launch Widget */
.quick-launch-widget .icon {
	font-size: var(--fontSize);
	padding: 0 4px;
    color: var(--text);
}

/* Quick Launch Popup - main window */

.quick-launch-popup .container {
	background-color: var(--background);
    border: 1px solid var(--border);
    border-radius: var(--border-radius);
}
/* Search bar container */
.quick-launch-popup .search {
	padding: 12px 16px;
	background-color: transparent;
	border-bottom: 1px solid var(--background2);
}
/* Search loader line color */
.quick-launch-popup .search .loader-line {
	color: var(--blue);
}
.quick-launch-popup .search .search-icon {
	font-family: var(--icons-font);
	font-size: 18px;
	color: var(--text);
	padding-right: 8px;
	min-width: 18px;
}
.quick-launch-popup .search .search-submit-icon {
	font-family: var(--icons-font);
	font-size: 18px;
	color: var(--text);
	min-width: 18px;
}
.quick-launch-popup .search .search-input {
	background: transparent;
	border: none;
	color: var(--text);
	font-size: var(--iconSize);
	font-family: var(--system-font);
	font-weight: var(--fontWeight);
	padding: 4px 0;
}
/* Search prefix styling (e.g., ">" for commands) */
.quick-launch-popup .search .prefix {
	background: var(--accent);
	border-radius: 6px;
	color: var(--text);
	padding: -2px 8px 0px 8px;
	margin-top: 2px;
	margin-right: 4px;
	font-size: 13px;
	font-weight: var(--fontWeight);
	font-family: var(--system-font);
	max-height: 28px;
}

/* Results list */
.quick-launch-popup .results {
	background: transparent;
	padding: 8px;
}
/* Individual result item here you can set font szie for title */
.quick-launch-popup .results-list-view {
	font-size: var(--fontSizeLarge);
	font-family: var(--system-font);
	font-weight: var(--fontWeight);
	color: var(--text);
}
.quick-launch-popup {
    background-color: var(--glass);
    border: 1px solid var(--border);
    border-radius: var(--border-radius);
    min-width: 480px;
}
.quick-launch-popup .results-list-view .description {
	color: var(--subtext);
	font-size: 11px;
	font-family: var(--system-font);
	font-weight: var(--fontWeight);
}
.quick-launch-popup .results-list-view .separator {
    color: var(--subtext);
    font-size: 13px;
    font-family: var(--system-font);
    font-weight: var(--fontWeight);
    padding: 4px 0 4px 12px;
}
/* Result item hover and selected states */
.quick-launch-popup .results-list-view::item {
	padding: 10px;
    margin-top: 4px;
	border-radius: var(--border-radius);
    margin-left: 4px;
    margin-right: 4px;
}
.quick-launch-popup .results-list-view::item:hover {
    background-color: var(--hover);
}
.quick-launch-popup .results-list-view::item:selected {
	background-color: var(--background2);
    border-radius: var(--border-radius);
}

.quick-launch-popup .results-list-view::item:selected:hover {
    background-color: var(--hover);
}

/* Empty state when no results found */
.quick-launch-popup .results-empty-text {
	font-size: 24px;
	font-family: var(--system-font);
	color: var(--text);
	padding-top: 8px;
}

/* CPU widget */
.cpu-widget .widget-container .icon {
    color: var(--mauve);
    padding-bottom: 1px;
}

.cpu-widget .widget-container .label {
    padding-left: 3px;
}
.cpu-widget .widget-container .label.alt {
    padding-left: 1.5px;
}

.cpu-widget {
    border: none;
}
/* Glazing Mocha CPU status colors */
.cpu-widget .label.status-low { color: var(--green); }
.cpu-widget .label.status-medium { color: var(--yellow); }
.cpu-widget .label.status-high { color: var(--peach); }
.cpu-widget .label.status-critical { color: var(--red); }

.cpu-popup {
    background-color: var(--glass);
    min-width: 400px;
    border: 1px solid var(--border);
    border-radius: var(--border-radius);
}

.cpu-popup .header {
    background: transparent;
    padding: 12px 16px;
    color: var(--text);
}
.cpu-popup .header .text {
    font-size: 16px;
    font-family: "Segoe UI";
    color: var(--text);
}
.cpu-popup .header .pin-btn {
    font-size: var(--fontSize);
    background: transparent;
    font-family: "Segoe Fluent Icons";
    padding: 6px;
    color: var(--text);
}
.cpu-popup .header .pin-btn:hover {
    color: var(--hover);
}
.cpu-popup .header .pin-btn.pinned {
    color: var(--accent);
}
/* Graph area */
.cpu-popup .graph-container {
    background:  transparent;
    min-height: 64px;
}
.cpu-popup .cpu-graph {
    color: var(--mauve);   /* <-- set the graph line/fill color */
}
.cpu-popup .cpu-graph-grid {
    color: var(--background2);  /* set the grid line color */
}
.cpu-popup .graph-title {
    font-size: 12px;
    color: var(--text);
    font-family: 'Segoe UI';
    padding: 0px 0px 4px 14px;
}
/* Stats grid */
.cpu-popup .stats {
    background: transparent;
    padding: 16px;
}
.cpu-popup .stats .stat-item {
    background-color: var(--background2);
    border: 1px solid var(--border);
    border-radius: var(--border-radius);
    padding: 8px 12px;
    margin: 8px;
}
.cpu-popup .stats .stat-label {
    font-size: 13px;
    color: var(--text);
    font-family: var(--system-font);
    font-weight: 400;
    padding: 6px 4px 2px 4px;
}
.cpu-popup .stats .stat-value {
    font-size: 20px;
    font-weight: 700;
    color: var(--subtext);
    font-family: var(--system-font);
    padding: 0 4px 12px 4px;
}

/* Memory widget */
.memory-widget .widget-container .label {
    padding-left: 3px;
    color: var(--text);
}
.memory-widget .widget-container .label.alt {
    padding-left: 1.5px;
}
.memory-widget .widget-container .icon {
    color: var(--blue);
    padding-bottom: 1px;
}

.memory-widget {
    border: none;
}
/* Glazing Mocha memory status colors */
.memory-widget .label.status-low { color: var(--green); }
.memory-widget .label.status-medium { color: var(--yellow); }
.memory-widget .label.status-high { color: var(--peach); }
.memory-widget .label.status-critical { color: var(--red); }

.memory-popup {
    background-color: var(--glass);
    min-width: 400px;
    border: 1px solid var(--border);
    border-radius: var(--border-radius);
}

.memory-popup .header {
    background: transparent;
    padding: 12px 16px;
}
.memory-popup .header .text {
    font-size: 16px;
    font-family: "Segoe UI";
    color: var(--text);
}
.memory-popup .header .pin-btn {
    font-size: 14px;
    background: transparent;
    font-family: "Segoe Fluent Icons";
    border: none;
    padding: 6px;
    color: var(--text);
}
.memory-popup .header .pin-btn:hover {
    color: var(--hover);
}
.memory-popup .header .pin-btn.pinned {
    color: var(--accent)
}
/* Graph area */
.memory-popup .graph-container {
    background:  transparent;
    min-height: 64px;
}
.memory-popup .memory-graph {
    color: var(--blue);   /* <-- set the graph line/fill color */
}
.memory-popup .memory-graph-grid {
    color: var(--background2);  /* set the grid line color */
}
.memory-popup .graph-title {
    font-size: 12px;
    color: var(--text);
    font-family: 'Segoe UI';
    padding: 0px 0px 4px 14px;
}
/* Stats grid */
.memory-popup .stats {
    background: transparent;
    padding: 16px;
}
.memory-popup .stats .stat-item {
    background-color: var(--background2);
    border: 1px solid var(--border);
    border-radius: var(--border-radius);
    padding: 8px 12px;
    margin: 8px;
}
.memory-popup .stats .stat-label {
    font-size: 13px;
    color: var(--text);
    font-family: var(--system-font);
    font-weight: 400;
    padding: 6px 4px 2px 4px;
}
.memory-popup .stats .stat-value {
    font-size: 20px;
    font-weight: 700;
    color: var(--subtext);
    font-family: var(--system-font);
    padding: 0 4px 12px 4px;
}

/* Alpha stats group - collapsible, Glazing Mocha */
.alpha-group .container { /* The name of the css class is the name given in the config */
    background-color: transparent;
}

.alpha-group .grouper-button {
    font-size: 18px;
    font-weight: 700;
    font-family: var(--system-font);
    color: var(--mauve);
    border: none;
    padding: 0 6px;
}

.alpha-group .grouper-button:hover {
    color: var(--text);
}

/* Control_Center */
/* POPUP WINDOW */

.control-center-widget .icon {
    color: var(--subtext1);
    font-family: var(--icons-font);
    font-size: 18px;
}

.control-center-menu {
    background: var(--glass);
    min-width: 360px;
    border: 1px solid var(--border);
    border-radius: var(--border-radius);
}

/* SECTIONS */

.control-center-menu .section {
    background: transparent;
    margin: 0;
    padding: 16px 12px;
    border: none;
}
/* We dont want a padding at the bottom of the first section. */
.control-center-menu .section.system-controls {
    padding: 12px 16px 0 16px;
}
.control-center-menu .section.sliders {
    padding: 16px;
}

/* SHARED SEGOE FLUENT ICONS */
.control-center-menu .section.system-controls .button,
.control-center-menu .section.quick-actions .button .icon,
.control-center-menu .section.sliders .slider .icon,
.control-center-menu .section.sliders .slider .source-selector,
.control-center-menu .section.power .plan-name .icon,
.control-center-menu .section.power .mode-name .icon,
.control-center-menu .section.media .button {
    font-family: "Segoe Fluent Icons";
    font-weight: 400;
}

/* SHARED HOVER & TRANSITION TRANSITIONS */
.control-center-menu .section.quick-actions .button .icon,
.control-center-menu .section.system-controls .button,
.control-center-menu .section.sliders .slider .source-selector,
.control-center-menu .section.power .plan-name,
.control-center-menu .section.power .mode-name,
.control-center-menu .section.media .button {
    transition: background-color 0.08s, opacity 0.08s;
    opacity: 1;
}

/* SHARED CLICKED / PRESSED STATES */
.control-center-menu .section.system-controls .button:clicked,
.control-center-menu .section.system-controls .button:pressed,
.control-center-menu .section.quick-actions .button .icon:clicked,
.control-center-menu .section.quick-actions .button .icon:pressed,
.control-center-menu .section.sliders .slider .source-selector:clicked,
.control-center-menu .section.sliders .slider .source-selector:pressed,
.control-center-menu .section.power .plan-name:clicked,
.control-center-menu .section.power .plan-name:pressed,
.control-center-menu .section.power .mode-name:clicked,
.control-center-menu .section.power .mode-name:pressed,
.control-center-menu .section.media .button:clicked,
.control-center-menu .section.media .button:pressed {
    opacity: 0.5;
}

/* SHARED DISABLED STATES */
.control-center-menu .section.quick-actions .button.disabled .title,
.control-center-menu .section.quick-actions .button.disabled .icon,
.control-center-menu .section.sliders .slider.disabled,
.control-center-menu .section.media .button.disabled,
.control-center-menu .section.media .button.disabled:hover {
    opacity: 0.5;
}

/* SYSTEM CONTROLS */
.control-center-menu .section.system-controls .button {
    background-color: var(--accent);
    border-radius: 16px;
    min-height: 32px;
    max-height: 32px;
    min-width: 32px;
    max-width: 32px;
    font-size: 14px;
    color: var(--accentText);
    transition: background-color 0.08s, opacity 0.08s;
}
.control-center-menu .section.system-controls .button:hover {
    background-color: var(--redFlash);
}

/* QUICK ACTIONS */
.control-center-menu .section.quick-actions .button {
    margin: 0 4px;
    cursor: pointer;
}
.control-center-menu .section.quick-actions .button .icon {
    font-size: 16px;
    background-color: var(--background2);
    min-height: 48px;
    border-radius: var(--border-radius);
    color: var(--text); 
}
.control-center-menu .section.quick-actions .button .icon:hover {
    background-color: var(--hover);
}
.control-center-menu .section.quick-actions .button.active .icon {
    background-color: var(--accent);
    color: var(--accentText);
}
.control-center-menu .section.quick-actions .button.active .icon:hover {
    background-color: var(--redFlash);
    color: var(--accentText);
}
.control-center-menu .section.quick-actions .button.disabled .icon:hover {
    background-color: var(--hover);
}
.control-center-menu .section.quick-actions .button.active .icon:pressed {
    background-color: var(--hover);
}
.control-center-menu .section.quick-actions .button .title {
    font-size: var(--fontSize);
    margin: 4px 0 8px 0;
    padding: 0;
    font-weight: var(--fontWeight);
    color: var(--text);
}

/* SLIDERS */
.control-center-menu .section.sliders .slider {
    background: transparent;
    border: none;
    min-height: 34px;
    margin: 0 4px 0 4px;
}
.control-center-menu .section.sliders .slider .icon {
    font-size: 16px;
    color: var(--text);
    min-width: 36px;
}
.control-center-menu .section.sliders .slider .value {
    min-width: 36px;
    font-size: 12px;
    font-weight: 600;
    color: var(--text);
}
.control-center-menu .section.sliders .slider .source-selector {
    font-size: 12px;
    color: var(--text);
    width: 24px;
    height: 24px;
    border-radius: 6px;
    background-color: var(--background);
    margin-left: 4px;
}
.control-center-menu .section.sliders .slider .source-selector:hover {
    background-color: var(--hover);
}

/* POWER PLAN & POWER MODE */
.control-center-menu .section.power .plan-name,
.control-center-menu .section.power .mode-name {
    background: var(--accent);
    border: 1px solid var(--border);
    border-radius: var(--border-radius);
    min-height: 36px;
    margin: 0 4px;
    padding: 6px 10px;
    cursor: pointer;
}
.control-center-menu .section.power .plan-name:hover,
.control-center-menu .section.power .mode-name:hover {
    background: var(--redFlash);
}
.control-center-menu .section.power .mode-name.disabled,
.control-center-menu .section.power .mode-name.disabled:hover {
    opacity: 0.5;
    background: var(--hover);
}
.control-center-menu .section.power .plan-name .title,
.control-center-menu .section.power .mode-name .title {
    font-size: var(--fontSize);
    font-weight: 600;
    color: var(--accentText);
}
.control-center-menu .section.power .plan-name .subtext,
.control-center-menu .section.power .mode-name .subtext {
    font-size: var(--fontSize);
    font-weight: 600;
    color: var(--accentText);
}

.control-center-menu .section.power .plan-name.disabled .title,
.control-center-menu .section.power .mode-name.disabled .title {
    font-size: var(--fontSize);
    font-weight: 600;
    color: var(--text);
}
.control-center-menu .section.power .plan-name.disabled .subtext,
.control-center-menu .section.power .mode-name.disabled .subtext {
    font-size: var(--fontSize);
    font-weight: 600;
    color: var(--text);
}
.control-center-menu .section.power .plan-name .icon,
.control-center-menu .section.power .mode-name .icon {
    color: var(--accentText);
    font-size: var(--iconSize);
}

.control-center-menu .section.power .plan-name.disabled .icon,
.control-center-menu .section.power .mode-name.disabled .icon {
    color: var(--text);
    font-size: var(--iconSize);
}

/* MEDIA CONTROLS */
.control-center-menu .section.media {
    background-color: transparent;
    padding: 12px;
}
.control-center-menu .section.media .track-info {
     padding-left: 8px;
}
.control-center-menu .section.media .title {
    font-size: var(--fontSize);
    font-weight: 600;
    color: var(--text);
}
.control-center-menu .section.media .subtext {
    font-size: var(--fontSize);
    font-weight: 600;
    color: var(--subtext);
}
.control-center-menu .section.media .button {
    font-size: var(--iconSize);
    background-color: var(--accent);
    color: var(--accentText);
    min-width: 32px;
    min-height: 32px;
    max-width: 32px;
    max-height: 32px;
    border-radius: 6px;
    margin: 0 0 0 4px;
}

.control-center-menu .section.media .button.prev {
    color: var(--accentText);
    background-color: var(--accent);
}
.control-center-menu .section.media .button.next {
    color: var(--accentText);
    background-color: var(--accent);
}

.control-center-menu .section.media .button.prev.disabled {
    color: var(--text);
}
.control-center-menu .section.media .button.next.disabled {
    color: var(--text);
}

.control-center-menu .section.media .button:hover {
    background-color: var(--redFlash);
}
.control-center-menu .section.media .button.disabled,
.control-center-menu .section.media .button.disabled:hover {
    background-color: var(--background2);
}

/* Context menu styles for dropdowns and menus inside the Control Center panel */
.control-center-menu .context-menu {
    background-color: var(--glass);
    padding: 4px 0px;
    font-family: "Segoe UI Variable", "Segoe UI";
    font-weight: var(--fontWeight);
    font-size: var(--fontSize);
    color: var(--text);
    border-radius: var(--border-radius);
    border: 1px solid var(--accent);
}
.control-center-menu .context-menu::item {
    background-color: transparent;
    padding: 6px 12px;
    margin: 2px 6px;
    border-radius: var(--border-radius3);
    min-width: 100px;
}
.control-center-menu .context-menu::item:selected  {
    background-color: var(--hover);
    color: var(--text);
}
.control-center-menu .context-menu::separator {
    height: 1px;
    background-color: var(--border);
    margin: 4px 0;
}
.control-center-menu .context-menu::indicator:unchecked {
    width: 4px;
    height: 12px;
    margin-left: 0;
    color: transparent;
    background-color: transparent;
}
.control-center-menu .context-menu::indicator:checked {
    width: 4px;
    height: 12px;
    background-color: var(--accent);
    border-radius: var(--border-radius3);
    margin-left: 0;
}

.cava-widget {
    padding: 0;
    margin: 0;
    padding-bottom: 1px;
}
.cava-widget .widget-container {}

/* Komorebi control + stack - glass menu, quiet buttons, active pill */
.komorebi-control-widget .widget-container .icon {
    color: var(--subtext1);
}
.komorebi-control-menu {
    background-color: var(--glass);
    border: 1px solid var(--border);
    border-radius: var(--border-radius);
    min-width: 220px;
}
.komorebi-control-menu .button {
    color: var(--subtext);
    padding: 8px 12px;
    margin: 2px 6px;
    font-size: 15px;
    border-radius: var(--border-radius2);
    background-color: transparent;
}
.komorebi-control-menu .button:hover {
    background-color: var(--hover);
    color: var(--text);
}
.komorebi-control-menu .button.active {
    color: var(--accent);
    background-color: var(--background2);
}
.komorebi-control-menu .button:disabled {
    color: var(--overlay0);
}
.komorebi-control-menu .footer {
    padding: 8px 12px;
    border-top: 1px solid var(--border);
}
.komorebi-control-menu .footer .text {
    font-size: 12px;
    font-family: var(--system-font);
    color: var(--subtext);
}
.komorebi-stack .window {
    background-color: transparent;
    border: none;
    margin: 0 2px;
    padding: 0 4px;
}
.komorebi-stack .window .label {
    font-size: 12px;
    color: var(--subtext);
}
.komorebi-stack .window .icon {
    padding-right: 2px;
}
.komorebi-stack .window.active {
    background-color: var(--background2);
    border-radius: var(--border-radius2);
}
.komorebi-stack .window.active .label {
    color: var(--text);
    font-weight: 600;
}

.yasb-bar .cpu-widget .widget-container .label,
.yasb-bar .gpu-widget .widget-container .label,
.yasb-bar .memory-widget .widget-container .label,
.yasb-bar .disk-widget .widget-container .label,
.yasb-bar .traffic-widget .widget-container .label {
    font-family: var(--icons-font);
    font-size: 12px;
    font-weight: 600;
    padding: 0 3px;
}
/* Traffic widget - compact */
.traffic-widget {
    padding-left: 4px;
    padding-right: 4px;
}
.traffic-widget .widget-container .label {
    padding-left: 2px;
    font-size: 11px;
    font-weight: 500;
    color: var(--subtext0);
}
.traffic-widget .widget-container .label span {
    font-family: var(--icons-font);
    font-size: 11px;
    color: var(--sky);
    padding: 0 2px;
}
.traffic-widget .widget-container .label.offline {
    color: var(--subtext);
    font-size: 11px;
}
.traffic-widget .widget-container .label.offline span {
    color: var(--redFlash);
}
.traffic-widget .widget-container .icon {
    font-size: 12px;
    color: var(--text);
    padding-bottom: 1px;
}
.traffic-widget .widget-container .icon.offline {
    color: var(--redFlash);
}

/* Traffic popup menu - matches cpu/memory popup + Kanagawa theme */
.traffic-menu {
    background-color: var(--glass);
    border: 1px solid var(--border);
    border-radius: var(--border-radius);
    min-width: 320px;
}
.traffic-menu .header {
    background: transparent;
    padding: 12px 16px 8px 16px;
    border-bottom: 1px solid var(--border);
}
.traffic-menu .header .title {
    font-size: 16px;
    font-family: var(--system-font);
    font-weight: 700;
    color: var(--text);
}
.traffic-menu .header .reset-button {
    font-size: var(--fontSize);
    font-family: var(--system-font);
    font-weight: var(--fontWeight);
    padding: 4px 10px;
    border-radius: var(--border-radius2);
    background-color: var(--background2);
    color: var(--text);
    border: 1px solid var(--border);
}
.traffic-menu .header .reset-button:hover {
    background-color: var(--hover);
    color: var(--text);
}
.traffic-menu .header .reset-button:pressed {
    background-color: var(--accent);
    color: var(--accentText);
}
/* Big live speeds at top */
.traffic-menu .download-speed,
.traffic-menu .upload-speed {
    background-color: transparent;
    padding: 12px 10px 4px 10px;
    margin: 0 12px;
    border-bottom: 1px solid var(--border);
}
.traffic-menu .speed-separator {
    max-width: 1px;
    background-color: var(--border);
    margin: 24px 0 12px 0;
}
.traffic-menu .upload-speed-value,
.traffic-menu .download-speed-value {
    font-size: 18px;
    font-weight: 800;
    font-family: var(--system-font);
    color: var(--text);
}
.traffic-menu .upload-speed-unit,
.traffic-menu .download-speed-unit {
    font-size: 13px;
    font-family: var(--system-font);
    font-weight: 600;
    color: var(--subtext);
    padding-top: 4px;
    padding-left: 4px;
}
.traffic-menu .upload-speed-placeholder,
.traffic-menu .download-speed-placeholder {
    color: var(--subtext);
    font-size: 11px;
    font-family: var(--system-font);
    padding: 0 0 8px 0;
}
/* Session / Today / All-time sections */
.traffic-menu .section-title {
    font-size: 12px;
    font-weight: 600;
    color: var(--subtext);
    margin-bottom: 4px;
    font-family: var(--system-font);
}
.traffic-menu .session-section,
.traffic-menu .today-section,
.traffic-menu .alltime-section {
    margin: 8px 8px 0 8px;
    padding: 0 10px 10px 10px;
    background-color: transparent;
    border-bottom: 1px solid var(--border);
}
.traffic-menu .alltime-section {
    border-bottom: none;
    margin-bottom: 8px;
}
.traffic-menu .data-text {
    font-size: 13px;
    color: var(--subtext);
    padding: 2px 0;
    font-family: var(--system-font);
}
.traffic-menu .data-value {
    font-weight: 600;
    font-size: 13px;
    color: var(--text);
    font-family: var(--system-font);
    padding: 2px 0;
}
/* Footer interface + internet status */
.traffic-menu .interface-info,
.traffic-menu .internet-info {
    font-size: 12px;
    font-family: var(--system-font);
    color: var(--subtext);
    padding: 8px 0;
}
.traffic-menu .internet-info.connected {
    background-color: var(--background2);
    color: var(--green);
}
.traffic-menu .internet-info.disconnected {
    background-color: var(--background2);
    color: var(--redFlash);
}
.traffic-menu .internet-info.checking {
    background-color: var(--background2);
    color: var(--subtext);
}

/* Omega quick-settings group - collapsible, Glazing Mocha */
.omega-group .container {
    background-color: transparent;
}
.omega-group .grouper-button {
    font-size: 18px;
    font-weight: 700;
    font-family: var(--system-font);
    color: var(--lavender);
    border: none;
    padding: 0 6px;
}
.omega-group .grouper-button:hover {
    color: var(--text);
}

/* WiFi - sky icon, ethernet handled by same widget */
.wifi-widget .widget-container .icon {
    color: var(--sky);
}
.wifi-widget .widget-container .label {
    color: var(--text);
}
.wifi-menu {
    background-color: var(--glass);
    border: 1px solid var(--border);
    border-radius: var(--border-radius);
    min-width: 360px;
}
.wifi-menu .header {
    padding: 10px 12px;
    border-bottom: 1px solid var(--border);
}
.wifi-menu .header .title {
    font-size: 14px;
    font-weight: 600;
    color: var(--text);
}
.wifi-menu .wifi-item {
    padding: 6px 12px;
    margin: 2px 6px;
    border-radius: var(--border-radius2);
}
.wifi-menu .wifi-item:hover {
    background-color: var(--hover);
}
.wifi-menu .wifi-item[active=true] {
    background-color: var(--background2);
}
.wifi-menu .wifi-item .icon {
    font-family: "Segoe Fluent Icons";
    font-size: 18px;
    color: var(--sky);
}
.wifi-menu .wifi-item .name {
    font-size: 13px;
    font-weight: 600;
    color: var(--text);
}
.wifi-menu .footer {
    font-size: 12px;
    font-family: var(--system-font);
    padding: 8px 12px;
    color: var(--subtext);
    border-top: 1px solid var(--border);
}

/* Battery - status colors */
.battery-widget .widget-container .icon {
    color: var(--green);
    padding-right: 3px;
}
.battery-widget .widget-container .label {
    color: var(--text);
}
.battery-widget .icon.status-critical,
.battery-widget .label.status-critical { color: var(--red); }
.battery-widget .icon.status-low,
.battery-widget .label.status-low { color: var(--peach); }
.battery-widget .icon.status-medium,
.battery-widget .label.status-medium { color: var(--yellow); }
.battery-widget .icon.status-high,
.battery-widget .label.status-high,
.battery-widget .icon.status-full,
.battery-widget .label.status-full { color: var(--green); }
.battery-widget .icon.status-charging,
.battery-widget .label.status-charging { color: var(--sky); }

/* Bluetooth - state colors */
.bluetooth-widget .widget-container .icon {
    font-family: "Segoe Fluent Icons";
}
.bluetooth-widget .icon.bt-off,
.bluetooth-widget .label.bt-off { color: var(--overlay0); }
.bluetooth-widget .icon.bt-on,
.bluetooth-widget .label.bt-on { color: var(--sky); }
.bluetooth-widget .icon.bt-connected,
.bluetooth-widget .label.bt-connected { color: var(--green); }
.bluetooth-menu {
    background-color: var(--glass);
    border: 1px solid var(--border);
    border-radius: var(--border-radius);
    min-width: 360px;
}
.bluetooth-menu .header {
    padding: 10px 12px;
    border-bottom: 1px solid var(--border);
}
.bluetooth-menu .header .title {
    font-size: 14px;
    font-weight: 600;
    color: var(--text);
}
.bluetooth-menu .section-title {
    font-size: 12px;
    font-weight: 600;
    color: var(--subtext);
    padding: 10px 12px 4px 12px;
}
.bluetooth-menu .bluetooth-item {
    padding: 6px 12px;
    margin: 2px 6px;
    border-radius: var(--border-radius2);
}
.bluetooth-menu .bluetooth-item:hover {
    background-color: var(--hover);
}
.bluetooth-menu .bluetooth-item.active {
    background-color: var(--background2);
}
.bluetooth-menu .bluetooth-item .icon {
    font-family: "Segoe Fluent Icons";
    font-size: 18px;
    color: var(--sky);
}
.bluetooth-menu .bluetooth-item .name {
    font-size: 13px;
    font-weight: 600;
    color: var(--text);
}
.bluetooth-menu .bluetooth-item .status {
    font-size: 12px;
    color: var(--subtext);
}
.bluetooth-menu .footer {
    font-size: 12px;
    font-family: var(--system-font);
    padding: 8px 12px;
    color: var(--subtext);
    border-top: 1px solid var(--border);
}

/* GPU - pink icon, Mocha status colors */
.gpu-widget .widget-container .icon {
    color: var(--pink);
    padding-bottom: 1px;
}
.gpu-widget .widget-container .label {
    color: var(--text);
}
.gpu-widget .label.status-low { color: var(--green); }
.gpu-widget .label.status-medium { color: var(--yellow); }
.gpu-widget .label.status-high { color: var(--peach); }
.gpu-widget .label.status-critical { color: var(--red); }
.gpu-popup {
    background-color: var(--glass);
    border: 1px solid var(--border);
    border-radius: var(--border-radius);
    min-width: 400px;
}
.gpu-popup .header {
    background: transparent;
    padding: 12px 16px 8px 16px;
    border-bottom: 1px solid var(--border);
}
.gpu-popup .header .text {
    font-size: 16px;
    font-weight: 700;
    font-family: var(--system-font);
    color: var(--text);
}
.gpu-popup .header .pin-btn {
    font-size: 14px;
    background: transparent;
    font-family: "Segoe Fluent Icons";
    border: none;
    padding: 6px;
    color: var(--subtext);
}
.gpu-popup .header .pin-btn:hover {
    color: var(--text);
}
.gpu-popup .header .pin-btn.pinned {
    color: var(--accent);
}
.gpu-popup .graph-container {
    background: transparent;
    min-height: 64px;
}
.gpu-popup .gpu-graph {
    color: var(--pink);
}
.gpu-popup .gpu-graph-grid {
    color: var(--background2);
}
.gpu-popup .gpu-temp-graph {
    color: var(--peach);
}
.gpu-popup .graph-title {
    font-size: 12px;
    color: var(--subtext);
    font-family: var(--system-font);
    padding: 0 0 4px 14px;
    margin-top: 12px;
}
.gpu-popup .graph-title.first {
    margin-top: 0;
}
.gpu-popup .stats {
    background: transparent;
    padding: 8px 12px 12px 12px;
}
.gpu-popup .stats .stat-item {
    background-color: var(--background2);
    border: 1px solid var(--border);
    border-radius: var(--border-radius2);
    padding: 8px 12px;
    margin: 4px;
}
.gpu-popup .stats .stat-label {
    font-size: 12px;
    color: var(--subtext);
    font-family: var(--system-font);
    padding: 4px 4px 2px 4px;
}
.gpu-popup .stats .stat-value {
    font-size: 20px;
    font-weight: 700;
    color: var(--text);
    font-family: var(--system-font);
    padding: 0 4px 8px 4px;
}

/* Disk - sapphire icon, Mocha status colors + group popup */
.disk-widget .widget-container .icon {
    color: var(--sapphire);
    padding-bottom: 1px;
}
.disk-widget .widget-container .label {
    color: var(--text);
}
.disk-widget .widget-container .label.status-low { color: var(--green); }
.disk-widget .widget-container .label.status-medium { color: var(--yellow); }
.disk-widget .widget-container .label.status-high { color: var(--peach); }
.disk-widget .widget-container .label.status-critical { color: var(--red); }
.disk-group {
    background-color: var(--background);
    border: 1px solid var(--border);
    border-radius: var(--border-radius);
    padding: 6px;
}
.disk-group {
    background-color: var(--glass);
    border: 1px solid var(--border);
    border-radius: var(--border-radius);
    padding: 10px 12px;
}
.disk-group-row {
    min-width: 220px;
    max-width: 260px;
    margin: 0;
    padding: 6px 8px;
    border-radius: var(--border-radius2);
    border: 1px solid transparent;
}
.disk-group-row:hover {
    background-color: var(--hover);
    border: 1px solid var(--border);
}
.disk-group-label {
    font-size: 12px;
    color: var(--text);
    font-family: var(--system-font);
}
.disk-group-label-size {
    font-size: 11px;
    color: var(--subtext);
    font-family: var(--system-font);
}
.disk-group-label-bar {
    max-height: 8px;
    border: none;
    background-color: var(--background2);
    border-radius: 4px;
}
.disk-group-label-bar::chunk {
    background-color: var(--sapphire);
    border-radius: 4px;
}


```

### Theme Config

```yaml
# yaml-language-server: $schema=https://raw.githubusercontent.com/amnweb/yasb/main/schema.json
# For more information, visit https://github.com/amnweb/yasb/wiki
watch_stylesheet: true
watch_config: true
system_colors: true
debug: false
update_check: true
bars:
  primary-bar:
    enabled: true
    style: "adaptive"
    screens:
    - '*'
    class_name: yasb-bar
    alignment:
      position: top
      align: center
    animation:
      enabled: true
      duration: 300
    blur_effect:
      enabled: true
      round_corners: true
    window_flags:
      always_on_top: false
      windows_app_bar: true
    dimensions:
      width: 100%
      height: 32
    padding:
      top: 8
      left: 12
      bottom: 0
      right: 12
    widgets:
      left:
      - home
      - lines
      - komorebi_active_layout
      - komorebi_control
      - lines
      - komorebi_workspaces
      - lines
      - active_window
      - komorebi_stack
      center:
      - clock
      - cava
      - media
      right:
      - systray
      - lines
      - alpha
      - lines
      - omega
      - lines
      - control_center
widgets:
  home:
    type: yasb.home.HomeWidget
    options:
      label: "<span>λ</span>"
      menu_list:
      - title: User Home
        path: '~'
      - title: Download
        path: ~\Downloads
      - title: Documents
        path: ~\Documents
      - title: Pictures
        path: ~\Pictures
      - title: Wallpapers
        path: D:\OneDrive\Pictures\Wallpapers\Themes
      system_menu: true
      power_menu: false
      blur: true
      round_corners: true
      round_corners_type: normal
      border_color: None
      alignment: left
      offset_left: -5
  omega:
    type: "yasb.grouper.GrouperWidget"
    options:
      class_name: "omega-group"
      # Ricing order (waybar/polybar convention, right-side cluster):
      # connectivity (wifi, bluetooth) -> audio (volume) -> power (battery)
      # -> appearance (wallpapers, palette) -> alerts (notifications last)
      widgets: [
        "wifi",
        "bluetooth",
        "volume",
        "battery",
        "wallpapers",
        "palette",
        "beta",
        "notifications",
      ]
      collapse_options:
        enabled: true
        expanded_label: "Ω"
        collapsed_label: "Ω"
        label_position: "right"
  clock:
    type: yasb.clock.ClockWidget
    options:
      label: '{%a, %d %b %H:%M}<span>{alarm}</span>'
      label_alt: '{%a, %d %b %H:%M}'
      timezones: []
      calendar:
        blur: true
        round_corners: true
        alignment: center
        direction: down
        extended: false
        show_years: true
        show_holidays: false
        show_week_numbers: true
      callbacks:
        on_left: toggle_calendar
  volume:
    type: yasb.volume.VolumeWidget
    options:
      label: "<span>{icon}</span> {level}"
      label_alt: "{level}"
      tooltip: true
      icons:
        "muted": "\uf026" # Icon for muted
        "10": "\uf026"  # Icon for 0-10% volume
        "30": "\uf026"  # Icon for 11-30% volume
        "60": "\uf026"  # Icon for 31-60% volume
        "100": "\uf026" # Icon for 61-100% volume
      callbacks:
        on_left: toggle_volume_menu
        on_right: toggle_mute
      audio_menu:
        blur: true
        round_corners: true
        round_corners_type: normal
        border_color: None
        alignment: right
        direction: down
        show_apps: true
        show_app_labels: true
        show_app_icons: true
        show_apps_expanded: false
        app_icons:
          toggle_down: "\uf107"
          toggle_up: "\uf106"
  notifications:
    type: yasb.notifications.NotificationsWidget
    options:
      label: "<span>\udb80\udc9e</span>"
      label_alt: '{count} notifications'
      hide_empty: true
      tooltip: false
      callbacks:
        on_left: toggle_notification
        on_right: do_nothing
        on_middle: do_nothing
  power_menu:
    type: yasb.power_menu.PowerMenuWidget
    options:
      label: "<span>\udb80\udc09</span>"
      uptime: true
      show_user: true
      menu_style: popup
      popup:
        blur: true
        round_corners: true
        round_corners_type: normal
        border_color: None
        alignment: right
        offset_left: 12
      profile_image_size: 64
      buttons:
        lock:
        - "\uDB80\uDF41"
        - Lock
        signout:
        - "\uDB80\uDF43"
        - Sign out
        sleep:
        - "\uDB82\uDD04"
        - Sleep
        hibernate:
        - "\uDB82\uDD01"
        - Hibernate
        restart:
        - "\uDB81\uDC53"
        - Restart
        shutdown:
        - "\uDB82\uDD06"
        - Shut Down
        cancel:
        - ''
        - Cancel
  active_window:
    type: yasb.active_window.ActiveWindowWidget
    options:
      label: ''
      label_alt: '{win[title]}'
      label_no_window: ''
      label_icon: true
      label_icon_size: 16
      max_length: 32
      max_length_ellipsis: '...'
      monitor_exclusive: true
  win_button:
      type: "yasb.custom.CustomWidget"
      options:
        label: "家"
        label_alt: "家"
        class_name: "system-widget"
        callbacks:
          on_left: "exec start_menu"
  lines:
    type: "yasb.custom.CustomWidget"
    options:
      label: "\u007c"
      label_alt: "\u007c"
      class_name: "separator-widget"
      callbacks:
        on_left: "do_nothing"
  palette:
    type: "yasb.custom.CustomWidget"
    options:
      label: "<span>वर्ण</span>"
      label_alt: "{data}"
      class_name: "home-widget"
      exec_options:
        run_cmd: "C:\\Users\\haris\\.config\\yasb\\tools\\theme\\yasb-theme.exe current"
        run_interval: 10000
        return_format: "string"
      callbacks:
        on_left: "exec silent-run C:\\Users\\haris\\.config\\yasb\\tools\\picker\\palette-picker.exe"
        on_middle: "toggle_label"
        on_right: "exec silent-run C:\\Users\\haris\\.config\\yasb\\tools\\theme\\yasb-theme.exe next"
  beta:
    type: "yasb.custom.CustomWidget"
    options:
      label: "<span>β</span>"
      label_alt: "{data}"
      class_name: "home-widget"
      exec_options:
        run_cmd: "C:\\Users\\haris\\.config\\yasb\\tools\\picker\\yasb-font.exe current"
        run_interval: 10000
        return_format: "string"
      callbacks:
        on_left: "exec silent-run C:\\Users\\haris\\.config\\yasb\\tools\\picker\\palette-picker.exe --fonts"
        on_middle: "toggle_label"
        on_right: "exec silent-run C:\\Users\\haris\\.config\\yasb\\tools\\picker\\yasb-font.exe next"
  komorebi_control:
    type: "komorebi.control.KomorebiControlWidget"
    options:
      label: "<span>\udb80\uddd9</span>"
      run_ahk: false
      run_whkd: false
      run_masir: false
      show_version: true
      komorebi_menu:
        blur: true
        round_corners: true
        round_corners_type: "normal"
        border_color: None
        alignment: "left"
        direction: "down"
        offset_top: 6
        offset_left: 0
  komorebi_stack:
    type: "komorebi.stack.StackWidget"
    options:
      label_offline: ""
      label_window: "{process}"
      label_window_active: "{process}"
      label_no_window: ""
      show_icons: "always"
      icon_size: 14
      max_length: 10
      max_length_active: 18
      hide_if_offline: true
      show_only_stack: true
      rewrite:
        - pattern: "^(.+?)\\.exe$"
          replacement: "\\1"
  komorebi_workspaces:
    type: "komorebi.workspaces.WorkspaceWidget"
    options:
      label_offline: "Komorebi Offline"
      label_workspace_btn: "{index}"
      label_workspace_active_btn: "{index}"
      label_workspace_populated_btn: "{index}"
      label_default_name: ""
      label_zero_index: false
      hide_empty_workspaces: true
      hide_if_offline: true
      toggle_workspace_layer:
        enabled: false
        tiling_label: "Tiling"
        floating_label: "Floating"
      app_icons: 
        enabled_populated: false
        enabled_active: false
        size: 12
        max_icons: 0
        hide_label: false
        hide_duplicates: false
        hide_floating: false
  komorebi_active_layout:
    type: "komorebi.active_layout.ActiveLayoutWidget"
    options:
      hide_if_offline: true
      label: "{layout_name}"
      layouts: ['bsp', 'columns', 'rows', 'grid', 'vertical_stack', 'horizontal_stack', 'ultrawide_vertical_stack','right_main_vertical_stack']
      layout_icons:
        bsp: "\uebeb"
        columns: "\uebf7"
        rows: "\uec01"
        grid: "\udb81\udf58"
        scrolling: "\uebf7"
        vertical_stack: "\uebee"
        horizontal_stack: "\uebf0"
        ultrawide_vertical_stack: "\uebee"
        right_main_vertical_stack: "\uebf1"
        monocle: "\uf06f"
        maximized: "\uf06f"
        floating: "\uf2d2"
        paused: "\udb83\udf89"
        tiling: "\udb81\ude40"
      callbacks:
        on_left: 'toggle_layout_menu'
        on_middle: 'next_layout'
        on_right: 'prev_layout'
      layout_menu:
        blur: true
        round_corners: true
        round_corners_type: "normal"
        border_color: None
        alignment: "left"
        direction: "down"
        offset_top: 6
        offset_left: 0
        show_layout_icons: true
  systray:
    type: "yasb.systray.SystrayWidget"
    options:
      class_name: "systray"
      label_collapsed: "▼"
      label_expanded: "▶"
      label_position: "left" # Can be "left" or "right"
      icon_size: 16 # Can be any integer between 8 and 64
      pin_click_modifier: "alt" # Can be "ctrl", "alt" or "shift"
      show_unpinned: false
      show_unpinned_button: true
      show_battery: false
      show_in_popup: true
      show_volume: false
      icons_per_row: 3
      # NOTE: show_network/use_hook each appeared twice (first value won nothing;
      # YAML keeps the last). Deduped to the effective values: no network icon
      # (wifi lives in omega), legacy systray monitor.
      show_network: false
      use_hook: false # Whether to use the new systray hook instead of the legacy systray monitor
      hide_icons: [] # Optional, list of process names to hide (e.g. ["discord"])
      popup:
        blur: true
        round_corners: true
        round_corners_type: "normal"
        border_color: None
        alignment: "center"
        direction: "down"
        offset_top: 6
        offset_left: 0
  wallpapers:
    type: "yasb.wallpapers.WallpapersWidget"
    options:
      label: "<span>\udb83\udc8d</span>"
      change_automatically: false
    # Example path to folder with images. Can be a single string or a list of strings.
      image_path: "H:\\8K wallpaper\\8K only" 
      engine:
        enabled: true
        animation: "slide_top" # circle/slide_top/diamond/split
      gallery:
        image_width: 520
        image_corner_radius: 6
        type: "magnified" # default/magnified/strip/slide - see "Gallery types" below
        orientation: "landscape" # landscape/portrait
        accent_color: "auto"
      callbacks:
        on_left: "toggle_gallery"
        on_middle: "do_nothing"
        on_right: "change_wallpaper"
      keybindings:
        - keys: "ctrl+alt+w"
          action: "toggle_gallery"
          screen: "primary" # active/cursor/primary
  media:
    type: "yasb.media.MediaWidget"
    options:
      label: "{title}{s}{artist}"
      label_alt: "{artist}"
      separator: " - "
      hide_empty: true
      callbacks:
        on_left: "toggle_media_menu"
        on_middle: "toggle_play_pause"
        on_right: "open_media_source"
      max_field_size:
        label: 45
        label_alt: 30
      show_thumbnail: true
      controls_only: false
      controls_left: true
      controls_hide: false
      thumbnail_alpha: 80
      thumbnail_padding: 8
      thumbnail_corner_radius: 16
      icons:
        prev_track: "\ue892"
        next_track: "\ue893"
        play: "\ue768"
        pause: "\ue769"
      media_menu:
        blur: true
        round_corners: true
        round_corners_type: "normal"
        border_color: None
        alignment: "center"
        direction: "down"
        offset_top: 6
        offset_left: -95
        thumbnail_corner_radius: 8
        thumbnail_size: 120
        max_title_size: 60
        max_artist_size: 50
        max_source_size: 16
        show_source: true
        show_volume_slider: true
      media_menu_icons:
        play: "\uf04b"
        pause: "\uf04c"
        prev_track: "\udb81\udcae"
        next_track: "\udb81\udcad"
        mute: "\ue994"
        unmute: "\ue74f"
      scrolling_label:
        enabled: true
        update_interval_ms: 33
        style: "bounce"  # can be "left", "right", "bounce", "bounce-ease"
        separator: " | "
        label_padding: 0
        always_scroll: false
      # Easing curve params: https://www.desmos.com/calculator/j7eamemxzi
        ease_slope: 20
        ease_pos: 0.8
        ease_min: 0.5
      progress_bar:
        enabled: true       # Whether to enable the progress bar on the widget.
        alignment: "bottom"  # The alignment of the progress bar inside the widget container. Can be "top", "bottom", or "center".
  language:
    type: "yasb.language.LanguageWidget"
    options:
      label: "{lang[language_code]}"
      label_alt: "{lang[full_name]}"
      update_interval: 1
      callbacks:
        on_left: "toggle_menu"
        on_middle: "do_nothing"
        on_right: "toggle_label"
      language_menu:
        blur: true
        round_corners: true
        round_corners_type: "normal"
        border_color: None
        alignment: "right"
        direction: "down"
        offset_top: 6
        offset_left: 0
        show_layout_icon: true
        layout_icon: "\udb80\udf0c"
  quick_launch:
    type: "yasb.quick_launch.QuickLaunchWidget"
    options:
      label: "<span>\uf002</span>"
      search_placeholder: "Search applications..."
      max_results: 30
      show_icons: true
      icon_size: 32
      popup:
        width: 650
        height: 400
        blur: true
        round_corners: true
        round_corners_type: "normal"
        border_color: None
        dark_mode: true
      callbacks:
        on_left: "toggle_quick_launch"
      keybindings:
        - keys: "alt+space"
          action: "toggle_quick_launch"
          screen: "primary"
  cpu:
    type: "yasb.cpu.CpuWidget"
    options:
      label: "<span>\uf085</span> {info[percent][total]}%"
      label_alt: "<span>\uf085</span> {info[freq][current]} MHz"
      update_interval: 2000
      hide_decimal: true
      cpu_thresholds:
        low: 25
        medium: 50
        high: 90
      histogram_icons:
        - "\u2581" # 0%
        - "\u2581" # 10%
        - "\u2582" # 20%
        - "\u2583" # 30%
        - "\u2584" # 40%
        - "\u2585" # 50%
        - "\u2586" # 60%
        - "\u2587" # 70%
        - "\u2588" # 80%+
      histogram_num_columns: 8
      callbacks:
        on_left: "toggle_menu"
        on_middle: "toggle_label"
        on_right: "toggle_label"
      menu:
        enabled: true
        show_graph: true
        show_graph_grid: true
        graph_history_size: 60
        round_corners: true
        round_corners_type: "normal"
        border_color: None
        alignment: "right"
        direction: "down"
        offset_top: 6
        offset_left: 0
        blur: true
  memory:
    type: "yasb.memory.MemoryWidget"
    options:
      label: "<span>\uf4bc</span> {virtual_mem_percent}%"
      label_alt: "<span>\uf4bc</span> {virtual_mem_used}/{virtual_mem_total} SWAP {swap_mem_percent}%"
      update_interval: 5000
      hide_decimal: true
      callbacks:
        on_left: "toggle_menu"
        on_middle: "toggle_label"
        on_right: "toggle_label"
      memory_thresholds:
        low: 25
        medium: 50
        high: 90
      histogram_icons:
        - "\u2581" # 0%
        - "\u2581" # 10%
        - "\u2582" # 20%
        - "\u2583" # 30%
        - "\u2584" # 40%
        - "\u2585" # 50%
        - "\u2586" # 60%
        - "\u2587" # 70%
        - "\u2588" # 80%+
      menu:
        enabled: true
        show_graph: true
        show_graph_grid: true
        graph_history_size: 60
        round_corners: true
        round_corners_type: "normal"
        border_color: None
        alignment: "right"
        direction: "down"
        offset_top: 6
        offset_left: 0
        blur: true
  traffic:
    type: "yasb.traffic.TrafficWidget"
    options:
      label: "<span>\ueab4</span> {download_speed} <span>\ueab7</span> {upload_speed}"
      label_alt: "DL {download_speed} UL {upload_speed} | Sess {session_downloaded}/{session_uploaded}"
      update_interval: 1000
      interface: "Auto"
      hide_if_offline: false
      speed_unit: "bytes"
      hide_decimal: true
      speed_threshold:
        min_upload: 0
        min_download: 0
      callbacks:
        on_left: "toggle_menu"
        on_middle: "toggle_label"
        on_right: "toggle_label"
      menu:
        blur: true
        round_corners: true
        round_corners_type: "normal"
        border_color: None
        alignment: "right"
        direction: "down"
        offset_top: 6
        offset_left: 0
        show_interface_name: true
        show_internet_info: true
  wifi:
    type: "yasb.wifi.WifiWidget"
    options:
      label: "<span>{wifi_icon}</span>"
      label_alt: "<span>{wifi_icon}</span> {wifi_name}"
      update_interval: 5000
      ethernet_label: "<span>{wifi_icon}</span>"
      ethernet_label_alt: "<span>{wifi_icon}</span> {ip_addr}"
      ethernet_icon: "\ueba9"
      get_exact_wifi_strength: false
      callbacks:
        on_left: "toggle_menu"
        on_middle: "toggle_label"
        on_right: "toggle_label"
      menu_config:
        blur: true
        round_corners: true
        round_corners_type: "normal"
        border_color: None
        alignment: "right"
        direction: "down"
        offset_top: 6
        offset_left: 0
  battery:
    type: "yasb.battery.BatteryWidget"
    options:
      label: "<span>{icon}</span> {percent}%"
      label_alt: "<span>{icon}</span> {percent}% | {time_remaining}"
      update_interval: 5000
      hide_unsupported: true
      time_remaining_natural: true
      charging_options:
        icon_format: "{charging_icon}"
        blink_charging_icon: true
        blink_interval: 500
      callbacks:
        on_left: "toggle_label"
        on_middle: "do_nothing"
        on_right: "do_nothing"
  bluetooth:
    type: "yasb.bluetooth.BluetoothWidget"
    options:
      label: "<span>{icon}</span>"
      label_alt: "<span>{icon}</span> {device_name}"
      tooltip: true
      callbacks:
        on_left: "toggle_menu"
        on_middle: "do_nothing"
        on_right: "toggle_label"
      menu_config:
        blur: true
        round_corners: true
        round_corners_type: "normal"
        border_color: None
        alignment: "right"
        direction: "down"
        offset_top: 6
        offset_left: 0
  gpu:
    type: "yasb.gpu.GpuWidget"
    options:
      label: "<span>\uf2db</span> {info[utilization]}%"
      label_alt: "<span>\uf2db</span> {info[temp]}°C | {info[mem_used]} / {info[mem_total]}"
      update_interval: 2000
      hide_decimal: true
      gpu_thresholds:
        low: 25
        medium: 50
        high: 90
      histogram_icons:
        - "\u2581"
        - "\u2581"
        - "\u2582"
        - "\u2583"
        - "\u2584"
        - "\u2585"
        - "\u2586"
        - "\u2587"
        - "\u2588"
      histogram_num_columns: 8
      callbacks:
        on_left: "toggle_menu"
        on_middle: "toggle_label"
        on_right: "toggle_label"
      menu:
        enabled: true
        blur: true
        round_corners: true
        round_corners_type: "normal"
        border_color: None
        alignment: "right"
        direction: "down"
        offset_top: 6
        offset_left: 0
        show_graph: true
        show_graph_grid: true
        graph_history_size: 60
  disk:
    type: "yasb.disk.DiskWidget"
    options:
      label: "<span>\uf473</span> C {space[used][percent]}"
      label_alt: "<span>\uf473</span> C {space[used][gb]} / {space[total][gb]}"
      volume_label: "C"
      decimal_display: 0
      update_interval: 60
      group_label:
        volume_labels: ["C", "H", "Z"]
        show_label_name: true
        blur: true
        round_corners: true
        round_corners_type: "normal"
        border_color: None
        alignment: "right"
        direction: "down"
        offset_top: 6
        offset_left: 0
      callbacks:
        on_left: "toggle_group"
        on_middle: "toggle_label"
        on_right: "toggle_label"
      disk_thresholds:
        low: 25
        medium: 50
        high: 90
  alpha:
    type: "yasb.grouper.GrouperWidget"
    options:
      class_name: "alpha-group"
      widgets: [
        "cpu",
        "gpu",
        "memory",
        "disk",
        "traffic",
      ]
      collapse_options:
        enabled: true
        expanded_label: "α"
        collapsed_label: "α"
        label_position: "right"
  control_center:
    type: "yasb.control_center.ControlCenterWidget"
    options:
      label: "<span>Θ</span>"
      tooltip: true
      sections_order:
        - "system_controls"
        - "quick_actions"
        - "sliders"
        - "power"
        - "media"
      popup:
        alignment: "right"
        direction: "down"
        border_color: none
        round_corners: false
        blur: true
        round_corners_type: normal
        offset_top: 9
        offset_left: 5
      sections:
        system_controls:
          profile_image_size: 28
          power_icon: "\uE7E8"
          lock_icon: "\uE72E"
          settings_icon: "\uE713"
        quick_actions:
          show: true
          columns: 3
          label_position: "default"
          actions:
            - id: "toggle_dnd"
              label: "Do Not Disturb"
              icon: "\uf285"
            - id: "toggle_mute"
              label: "Mute"
              icon: "\ue74f"
            - id: "toggle_mic_mute"
              label: "Mic Mute"
              icon: "\uF12E"
            - id: "screenshot"
              label: "Screenshot"
              icon: "\ue91b"
            - id: "touch_keyboard"
              label: "Keyboard"
              icon: "\uE765"
            - id: "toggle_theme"
              label: "Dark Mode"
              icon: "\uE708"
        sliders:
          show: true
          brightness:
            show_slider: true
            icon: "\uE706"
            show_source_selector: true
            source_selector_icon: "\uE972"
          volume:
            show_slider: true
            icon: "\uE767"
            show_source_selector: true
            source_selector_icon: "\uE972"
          microphone:
            show_slider: true
            icon: "\uE720"
            show_source_selector: true
            source_selector_icon: "\uE972"
        media:
          show: true
          thumbnail_size: 36
          thumbnail_radius: 4
          icons:
            prev_track: "\ue622"
            next_track: "\ue623"
            play: "\uf5b0"
            pause: "\ue62e"
        power:
          show: true
          power_plan_title: "Power Plan"
          power_mode_title: "Power Mode"
          button_menu_icon: "\ue76c"
      callbacks:
        on_left: "toggle_menu"
  cava:
    type: "yasb.cava.CavaWidget"
    options:
      source: "auto"
      bar_height: 22
      min_bar_height: 2
      bars_number: 20
      bar_width: 2
      bar_spacing: 2
      bar_type: "bars_mirrored"
      orientation: "bottom"
      sensitivity: 100
      lower_cutoff_freq: 50
      higher_cutoff_freq: 12000
      framerate: 60
      noise_reduction: 77
      channels: stereo
      mono_option: average
      reverse: 0
      monstercat: 0
      waves: 0
      waveform: 0
      sleep_timer: 5
      hide_empty: true
      foreground: "#7AA89F"
      gradient: 1
      gradient_color_1: "#7E9CD8"
      gradient_color_2: "#957FB8"
      gradient_color_3: "#FFA066"
      callbacks:
        on_left: "do_nothing"
        on_middle: "do_nothing"
        on_right: "reload_cava"
```

### Readme

# Rangalipi

![Theme Preview](PREVIEW_PNG_URL)

Kanagawa-wave dark bar on floating glass islands with gold borders. Komorebi
workspaces, system stats, media with full controls, and two suckless pickers:
one for 82 color palettes, one for installed Nerd Fonts.

## Features

- **Liquid glass**: theme-tinted blur on bar islands and every popup
- **Palette browser (वर्ण)**: scrollable flexbox switcher for 82 palettes,
  live search, arrows + Enter, chrome follows the active theme
- **Font browser (β)**: switch any installed Nerd Font live, names previewed
  in their own typeface
- **Komorebi first**: workspaces, active layout, control, stack widgets
- **Full media**: thumbnail, inline controls, bounce titles, progress line,
  volume slider, play/pause + open-player mouse actions
- **System monitors**: CPU, GPU, memory, disk, traffic in one collapsible
  group with integer readouts and load-status colors
- **Zero flash**: every launcher routed through a hidden runner process
- **RDP-proof**: remote windows ignored by class, exe and title so sessions
  never disturb tiling or focus
- **Boot-proof**: ordered login chain (Komorebi, GlazeWM keys, bar) with a
  one-shot setup script that rebuilds and verifies everything

## Bar layout

Left: home menu, Komorebi layout + control, workspaces, active-window icon,
stack. Center: clock, cava spectrum (theme-synced gradient), media. Right:
systray, system-stats group (α), control group (Ω: network, audio, power,
wallpapers, palette, fonts, alerts), control center (Θ).

## Installation

1. **Fonts**: install `Hack Nerd Font` (or any Nerd Font), `Segoe UI Variable`,
   `Segoe Fluent Icons`. The bar falls back gracefully without them.
2. Copy `config.yaml` and `styles.css` into `%USERPROFILE%\.config\yasb`.
   Tested on YASB v2.0.7, Komorebi 0.1.41, GlazeWM 3.10.1.
3. Companion tools ship as source only (no binaries) under `tools\`
   (theme CLI, palette and font pickers) and `yasb-theme\` (Rust source).
   Build every exe with `tools\setup\yasb-setup.ps1` — Rust, Qt6 and
   PyInstaller are installed automatically when missing. Without them the
   bar still works; only the वर्ण/β buttons need rebinding. WM configs
   live in `configs\`.

### Companion scripts

All runnable from PowerShell (`-ExecutionPolicy Bypass` for `.ps1`):

- `tools\setup\yasb-setup.ps1` — one-shot setup: checks toolchains
  (Rust, Python Qt6), rebuilds every binary, verifies the chain, snapshots
  the WM configs. Idempotent, safe to re-run.
- `tools\theme\yasb-theme-build.ps1` — rebuilds `yasb-theme.exe`
  (`list|current|set|next|prev`) and deploys `silent-run.exe`.
- `tools\theme\yasb-theme-shell.ps1` — dot-source for the `yt` shortcut.
- `tools\picker\palette-picker-build.ps1` — rebuilds `palette-picker.exe`.
- `tools\picker\yasb-font-build.ps1` — rebuilds `yasb-font.exe`
  (`list|current|set|next|prev` over installed Nerd Fonts).
- `tools\setup\export-theme.py` — regenerates this submission pack
  (single-theme CSS, clean config, redaction, screenshots).

## Author

[![GitHub](https://img.shields.io/badge/GitHub-harish2222-181717?logo=github&style=flat-square)](https://github.com/harish2222)
