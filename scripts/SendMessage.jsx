import React, { Component } from 'react';
import { Form, Message } from 'semantic-ui-react';
import PropTypes from 'prop-types';
import Socket from './Socket';

export default class SendMessage extends Component {
    constructor(props) {
        super(props);

        this.state = {
            message: '',
        };
    }

    handleSubmit = (event) => {
        const { login, name, avatar } = this.props;
        const { message } = this.state;
        if (login) {
            Socket.emit('new message input', {
                message,
                name,
                avatar,
            });

            this.setState({
                message: '',
            });
        }

        event.preventDefault();
    }

    handleChange = (event) => {
        this.setState({
            message: event.target.value,
        });
    }

    render() {
        const { message } = this.state;
        const { login } = this.props;
        return (
            <Form error onSubmit={this.handleSubmit}>
                <Form.Group>
                    <Form.Input placeholder="Enter your message..." width={13} onChange={this.handleChange} value={message} />
                    <Form.Button width={3}>Send</Form.Button>
                </Form.Group>
                {
                    !login && (
                        <Message
                            error
                            header="Action Forbidden"
                            content="You can only sign up for an account once with a given e-mail address."
                        />
                    )
                }
            </Form>
        );
    }
}

SendMessage.propTypes = {
    login: PropTypes.bool,
    avatar: PropTypes.string,
    name: PropTypes.string,
};

SendMessage.defaultProps = {
    login: false,
    avatar: '',
    name: '',
};
