const {app, BrowserWindow} = require("electron");

function ElectronMainMethod(){
    const launchWindow = new BrowserWindow({
        title: "CRM-Project",
        width: 777,
        height: 555,
    });
    const appURL = "http://localhost:8000";
    launchWindow.loadURL(appURL);
}//end main()

app.whenReady().then(ElectronMainMethod)