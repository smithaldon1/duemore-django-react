import React, { Component } from 'react';


export default class TaskList extends Component {
    state = {
        tasks: [],
    };

    async componentDidMount() {
        try {
            const res = await fetch('http://127.0.0.1:8000/api/task/');
            const tasks = await res.json();
            this.setState({
                tasks
            });
        } catch (e) {
            console.log(e)
        }
    }

    render() {
        return (
            <div>
                {this.state.tasks.map(item => (
                    <>
                        <div key={item.task_id}>
                            <h1>{item.name}</h1>
                            <p>{item.description}</p>
                        </div>
                        <input type="text" value={item.name} formMethod="POST" />
                    </>
                ))}
            </div>
        );
    }
}