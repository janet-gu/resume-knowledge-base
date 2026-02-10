import React from 'react';
import { BrowserRouter as Router, Route, Switch, Link } from 'react-router-dom';

const Home = () => <div>Home Page</div>;
const About = () => <div>About Page</div>;
const Contact = () => <div>Contact Page</div>;

const App = () => {
    return (
        <Router>
            <nav>
                <ul>
                    <li><Link to="/">Home</Link></li>
                    <li><Link to="/about">About</Link></li>
                    <li><Link to="/contact">Contact</Link></li>
                </ul>
            </nav>
            <Switch>
                <Route path="/about" component={About} />
                <Route path="/contact" component={Contact} />
                <Route path="/" component={Home} />
            </Switch>
        </Router>
    );
};

export default App;