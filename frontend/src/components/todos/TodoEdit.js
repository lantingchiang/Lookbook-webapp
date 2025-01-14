// components/todos/TodoEdit.js

import _ from 'lodash';
import React, { Component } from 'react';
import { connect } from 'react-redux';
import { getTodos, editTodo } from '../../actions/todos';
import TodoForm from './TodoForm';

class TodoEdit extends Component {
    componentDidMount() {
        this.props.getTodos(this.props.match.params.id);
    }

    onSubmit = formValues => {
        this.props.editTodo(this.props.match.params.id, formValues);
    };

    render() {
        return (
            <div className='ui container'>
                <h2 style={{ marginTop: '2rem' }}>Edit Todo</h2>
                <TodoForm
                    initialValues={_.pick(this.props.todo, 'task')}
                    enableReinitialize={true}
                    onSubmit={this.onSubmit}
                />
            </div>
        );
    }
}

const mapStateToProps = (state, ownProps) => ({
    todo: state.todos[ownProps.match.params.id]
});

export default connect(
    mapStateToProps,
    { getTodos, editTodo }
)(TodoEdit);