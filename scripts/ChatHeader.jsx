import React, { Component } from 'react';
import { GoogleLogin, GoogleLogout } from 'react-google-login'
import { Header, Grid, Label, Ref } from 'semantic-ui-react'

export class ChatHeader extends Component {
    constructor(props) {
        super(props);

        this.clientId = "564574908714-sh0i2elo3a2a1dfh5lpec354du76hk28.apps.googleusercontent.com";
        this.ref = React.createRef();
    }

    render() {
        return (
            <Grid verticalAlign='middle'>
                <Grid.Row>
                    <Grid.Column floated='left' width={8}>
                        <Header as='h2'>Chat Room</Header>
                    </Grid.Column>
                    <Grid.Column width={5} textAlign='right'>
                        {
                            !this.props.login && <GoogleLogin
                                clientId={this.clientId}
                                buttonText="Sign in"
                                onSuccess={this.props.onLoginSuccess}
                                onFailure={this.props.onLoginFailure}
                                cookiePolicy={'single_host_origin'}
                                isSignedIn={true}
                            />
                        }
                        {
                            this.props.login && <GoogleLogout
                                clientId={this.clientId}
                                buttonText="Logout"
                                onLogoutSuccess={this.props.onLogoutSuccess}
                            />
                        }
                    </Grid.Column>
                </Grid.Row>
                {this.props.login &&
                    <Grid.Row>
                        <Grid.Column floated='left' width={16}>
                            <Label as='a' color='blue' image>
                                <img src={this.props.avatar} />
                                {this.props.name}
                                <Label.Detail>{this.props.email}</Label.Detail>
                            </Label>
                        </Grid.Column>
                    </Grid.Row>
                }
            </Grid>
        );
    }
}