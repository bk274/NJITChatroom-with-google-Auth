import React, { Component } from 'react';
import { ChatHeader } from './ChatHeader';
import { Socket } from './Socket';
import { SendMessage } from './SendMessage';
import { Segment, Comment, Divider, Icon, Image, Ref } from 'semantic-ui-react';

export class Content extends Component {

    constructor(props) {
        super(props);

        this.state = {
            messages: [],
            users: 0,
            name: "invalid",
            avatar: "",
            email: "invalid",
            login: false,
            id: 0
        };
        
        
        this.ref = React.createRef();

    }

    componentDidUpdate() {
        this.ref.current.scrollTop = this.ref.current.scrollHeight
    }

    UNSAFE_componentWillMount() {
        Socket.on('messages received', (data) => {
            this.setState({
                messages: data['messages'],
                users: data['users']
            });

            console.log("Received messages from server: " + data['messages']);
        });
    }

    onLoginSuccess = (res) => {
        const profile = res.profileObj;

        this.setState({
            name: profile.name,
            avatar: profile.imageUrl,
            email: profile.email,
            login: true,
            id: profile.googleId
        })
        console.log('[Login Success] currentUser', res.profileObj);

        Socket.emit('new user input', {
            'id': profile.googleId,
        });
    }

    onLoginFailure = (res) => {
        console.log('[Login failed] res:', res);
    }

    onLogoutSuccess = () => {

        this.setState({
            name: "invalid",
            email: "invalid",
            avatar: "",
            login: false
        });
        console.log('Logout made successfully');

        Socket.emit('new user output', {
            'id': this.state.id,
        });
    }
    
    componentWillUnmount() {
        this.onLogoutSuccess();
    }

    isValidURL = str => {
        const pattern = new RegExp('^(https?:\\/\\/)?' + // protocol
            '((([a-z\\d]([a-z\\d-]*[a-z\\d])*)\\.)+[a-z]{2,}|' + // domain name
            '((\\d{1,3}\\.){3}\\d{1,3}))' + // OR ip (v4) address
            '(\\:\\d+)?(\\/[-a-z\\d%_.~+]*)*' + // port and path
            '(\\?[;&a-z\\d%_.~+=-]*)?' + // query string
            '(\\#[-a-z\\d_]*)?$', 'i'); // fragment locator

        return !!pattern.test(str);
    }

    isImageUrl = str => {
        const upperCase = str.toUpperCase();

        return upperCase.endsWith("JPG") || upperCase.endsWith("PNG") || upperCase.endsWith("GIF");
    }

    render() {
        return (
            <Segment padded>
                <ChatHeader onLoginSuccess={this.onLoginSuccess} onLoginFailure={this.onLoginFailure} onLogoutSuccess={this.onLogoutSuccess}
                    name={this.state.name} avatar={this.state.avatar} email={this.state.email} login={this.state.login} />

                <Ref innerRef={this.ref}>
                    <Segment style={{ overflow: 'auto', maxHeight: '40vh', minHeight: '40vh' }}>
                        <Comment.Group>
                            {this.state.messages.map((message) =>
                                <Comment key={message[1]}>
                                    <Comment.Avatar src={message[3]} />
                                    <Comment.Content>
                                        <Comment.Author as='a'>{message[2]}</Comment.Author>
                                        <Comment.Metadata>
                                            <div>{message[1]}</div>
                                        </Comment.Metadata>
                                        <Comment.Text>
                                            {this.isValidURL(message[0]) ?
                                                (<a href={message[0]}>
                                                    {this.isImageUrl(message[0]) ?
                                                        <Image src={message[0]} size='small' />
                                                        : message[0]}
                                                </a>)
                                                : message[0]}
                                        </Comment.Text>
                                    </Comment.Content>
                                </Comment>

                            )}
                        </Comment.Group>
                    </Segment>
                </Ref>
                <SendMessage name={this.state.name} avatar={this.state.avatar} login={this.state.login} />

                <Divider section />

                <a>
                    <Icon name='user' />
                    {this.state.users}
                </a>
            </Segment>
        );
    }
}

