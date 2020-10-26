import React, { Component } from 'react';
import { Socket } from './Socket';
import { Form, Message } from 'semantic-ui-react'

export class SendMessage extends Component {
    constructor(props) {
        super(props);

        this.state = {
            message: ""
        };

        console.log(this.props.login)
    }

    handleSubmit = event => {
        if (this.props.login) {
            Socket.emit('new message input', {
                'message': this.state.message,
                'name': this.props.name,
                'avatar': this.props.avatar
            });

            this.setState({
                message: ""
            });
            console.log('Sent the message ' + this.state.message + ' to server');
        }

        event.preventDefault();
    }

    handleChange = event => {
        this.setState({
            message: event.target.value
        });
    }

    render() {
        return (
            <Form error onSubmit={this.handleSubmit}>
                <Form.Group>
                    <Form.Input placeholder='Enter your message...' width={13} onChange={this.handleChange} value={this.state.message} />
                    <Form.Button width={3}>Send</Form.Button>
                </Form.Group>


                {
                    !this.props.login && <Message
                        error
                        header='Action Forbidden'
                        content='You can only sign up for an account once with a given e-mail address.'
                    />
                }
            </Form>
        );
    }
}