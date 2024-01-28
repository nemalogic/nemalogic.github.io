/*
 * This file launches the application by asking Ext JS to create
 * and launch() the Application class.
 */
Ext.application({
    extend: 'Fifa_app.Application',

    name: 'Fifa_app',

    requires: [
        // This will automatically load all classes in the Fifa_app namespace
        // so that application classes do not need to require each other.
        'Fifa_app.*'
    ],

    // The name of the initial view to create.
    mainView: 'Fifa_app.view.main.Main'
});
