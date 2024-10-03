#!/bin/bash

function install_template {
    echo_summary "install template"
    echo "templatecloud plugin work install" >> templateplugin.log

}

function init_template {
    echo_summary "init template"
    echo "templatecloud plugin work init" >> templateplugin.log
}

function configure_template {
    echo_summary "configuring template"
    echo "templatecloud plugin work template" >> templateplugin.log
}

# check for service enabled
if is_service_enabled templatecloud; then

    if [[ "$1" == "stack" && "$2" == "pre-install" ]]; then
        # Set up system services
        echo_summary "Configuring templatecloud"
        install_package cowsay

    elif [[ "$1" == "stack" && "$2" == "install" ]]; then
        # Perform installation of service source
        echo_summary "Installing templatecloud"
        install_template

    elif [[ "$1" == "stack" && "$2" == "post-config" ]]; then
        # Configure after the other layer 1 and 2 services have been configured
        echo_summary "Configuring templatecloud"
        configure_template

    elif [[ "$1" == "stack" && "$2" == "extra" ]]; then
        # Initialize and start the template service
        echo_summary "Initializing templatecloud"
        init_template
    fi

    if [[ "$1" == "unstack" ]]; then
        echo_summary "Unstack templatecloud"

        # Shut down template services
        # no-op
        :
    fi

    if [[ "$1" == "clean" ]]; then
        echo_summary "Clean templatecloud"
        # Remove state and transient data
        # Remember clean.sh first calls unstack.sh
        # no-op
        :
    fi
fi

