import React, { Component } from 'react';
import {
    Segment, Comment, Divider, Icon, Image, Ref,
} from 'semantic-ui-react';
import ChatHeader from './ChatHeader';
import Socket from './Socket';
import SendMessage from './SendMessage';

export default class Content extends Component {
    constructor(props) {
        super(props);

        this.state = {
            messages: [],
            users: 0,
            name: 'invalid',
            avatar: '',
            email: 'invalid',
            login: false,
            id: 0,
        };
        this.ref = React.createRef();

        Socket.on('messages received', (data) => {
            this.setState({
                messages: data.messages,
                users: data.users,
            });
        });
    }

    componentDidUpdate() {
        this.ref.current.scrollTop = this.ref.current.scrollHeight;
    }

    componentWillUnmount() {
        this.onLogoutSuccess();
    }

    onLoginSuccess = (res) => {
        const profile = res.profileObj;

        this.setState({
            name: profile.name,
            avatar: profile.imageUrl,
            email: profile.email,
            login: true,
            id: profile.googleId,
        });

        Socket.emit('new user input', {
            id: profile.googleId,
        });
    }

    onLoginFailure = () => {
    }

    onLogoutSuccess = () => {
        this.setState({
            name: 'invalid',
            email: 'invalid',
            avatar: '',
            login: false,
        });

        const { id } = this.state;
        Socket.emit('new user output', {
            id,
        });
    }

    isValidURL = (str) => {
        const pattern = new RegExp('^(https?:\\/\\/)?' // protocol
            + '((([a-z\\d]([a-z\\d-]*[a-z\\d])*)\\.)+[a-z]{2,}|' // domain name
            + '((\\d{1,3}\\.){3}\\d{1,3}))' // OR ip (v4) address
            + '(\\:\\d+)?(\\/[-a-z\\d%_.~+]*)*' // port and path
            + '(\\?[;&a-z\\d%_.~+=-]*)?' // query string
            + '(\\#[-a-z\\d_]*)?$', 'i'); // fragment locator

        return !!pattern.test(str);
    }

    isImageUrl = (str) => {
        const upperCase = str.toUpperCase();

        return upperCase.endsWith('JPG') || upperCase.endsWith('PNG') || upperCase.endsWith('GIF');
    }

    render() {
        const {
            name, avatar, email, login, messages, users,
        } = this.state;
        return (
            <Segment padded>
                <ChatHeader
                    onLoginSuccess={this.onLoginSuccess}
                    onLoginFailure={this.onLoginFailure}
                    onLogoutSuccess={this.onLogoutSuccess}
                    name={name}
                    avatar={avatar}
                    email={email}
                    login={login}
                />

                <Ref innerRef={this.ref}>
                    <Segment style={{ overflow: 'auto', maxHeight: '40vh', minHeight: '40vh' }}>
                        <Comment.Group>
                            {messages.map((message) => (
                                <Comment key={message[1]}>
                                    <Comment.Avatar src={message[3]} />
                                    <Comment.Content>
                                        <Comment.Author as="a">{message[2]}</Comment.Author>
                                        <Comment.Metadata>
                                            <div>{message[1]}</div>
                                        </Comment.Metadata>
                                        <Comment.Text>
                                            {this.isValidURL(message[0]) ? (
                                                <a href={message[0]}>
                                                    {this.isImageUrl(message[0]) ? (
                                                        <Image src={message[0]} size="small" />
                                                    )
                                                    : message[0]}
                                                </a>
                                            )
                                            : message[0]}
                                        </Comment.Text>
                                    </Comment.Content>
                                </Comment>
                            ))}
                        </Comment.Group>
                    </Segment>
                </Ref>
                <SendMessage
                    name={name}
                    avatar={avatar}
                    login={login}
                />

                <Divider section />

                <Icon name="user" />
                {users}
            </Segment>
        );
    }
}
