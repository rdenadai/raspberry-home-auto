import React, { Component } from 'react';
// import { Link } from 'react-router';
import { connect } from 'react-redux';

// import {Card, CardActions, CardMedia, CardTitle, CardText} from 'material-ui/Card';
// import FlatButton from 'material-ui/FlatButton';

class LandingPage extends Component {

    constructor(props) {
        super(props);
    }

    render() {
        return (
            <div>Landing Page</div>
        );
    }
}

export default connect()(LandingPage);
