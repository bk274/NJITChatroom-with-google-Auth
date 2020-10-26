import React, { useState } from 'react';
import { useEffect } from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Paper from '@material-ui/core/Paper';
import Typography from '@material-ui/core/Typography';
import Button from '@material-ui/core/Button';
import TextField from '@material-ui/core/TextField';
import * as SocketIO from 'socket.io-client';
import './Styles.css';
import ScrollToBottom from 'react-scroll-to-bottom';

const useStyles = makeStyles(layout => ({
    root: {
        margin: '100px',
        padding: layout.spacing(5, 2),
        width: '600px',
    },
    flex: {
        display: 'flex',
    },
    chat_window: {
        width: '100%',
        height: '300px',
        textAlign: 'right',
        padding: '3px',
        overflowY: 'auto',
        overflowX: 'hidden',
        flex: 'row-reverse'
    },
    chat_box: {
        width: '90%'  
    },
    chat_button: {
        width: '10%'
        },

}));