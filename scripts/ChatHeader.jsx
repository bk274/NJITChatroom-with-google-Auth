import React, { Component } from 'react';
import { GoogleLogin, GoogleLogout } from 'react-google-login';
import { Header, Grid, Label } from 'semantic-ui-react';
import PropTypes from 'prop-types';

export default class ChatHeader extends Component {
    constructor(props) {
        super(props);

        this.clientId = '1075433900902-3m8ufv68sq71h30ebnc4d04aikeoo3ut.apps.googleusercontent.com';
    }

    render() {
        const {
            login, onLoginSuccess, onLoginFailure,
            onLogoutSuccess, avatar, name, email,
        } = this.props;

        return (
            <Grid verticalAlign="middle">
                <Grid.Row>
                    <Grid.Column floated="left" width={8}>
                        <Header as="h2">Chat Room</Header>
                    </Grid.Column>
                    <Grid.Column width={5} textAlign="right">
                        {
                            !login && (
                                <GoogleLogin
                                    clientId={this.clientId}
                                    buttonText="Sign in"
                                    onSuccess={onLoginSuccess}
                                    onFailure={onLoginFailure}
                                    cookiePolicy="single_host_origin"
                                    isSignedIn
                                />
                            )
                        }
                        {
                            login && (
                                <GoogleLogout
                                    clientId={this.clientId}
                                    buttonText="Logout"
                                    onLogoutSuccess={onLogoutSuccess}
                                />
                            )
                        }
                    </Grid.Column>
                </Grid.Row>
                {
                    login && (
                        <Grid.Row>
                            <Grid.Column floated="left" width={16}>
                                <Label as="a" color="blue" image>
                                    <img src={avatar} alt="avatar" />
                                    {name}
                                    <Label.Detail>{email}</Label.Detail>
                                </Label>
                            </Grid.Column>
                        </Grid.Row>
                    )
                }
            </Grid>
        );
    }
}

ChatHeader.propTypes = {
    login: PropTypes.bool,
    avatar: PropTypes.string,
    name: PropTypes.string,
    email: PropTypes.string,
    onLoginSuccess: PropTypes.func,
    onLoginFailure: PropTypes.func,
    onLogoutSuccess: PropTypes.func,
};

ChatHeader.defaultProps = {
    login: false,
    avatar: '',
    name: '',
    email: '',
    onLoginSuccess: () => { },
    onLoginFailure: () => { },
    onLogoutSuccess: () => { },
};
