Which of the following statements is true regarding React.js?

Answer:

� React is just another MVC framework

oO Every React component is stateless

oO Shallow rendering in React allows you to render a single component completely

� TDD is not allowed when writing React components
Which of the following statements is true regarding the following component?
```
class MyComponent extends React.Component {
 render()}{
  return (This is a component);
 }
}
```
Answer:

� Render should not be a function

� Render method is not required

O The return should be any React element, null or false

O Class should be replaced by className
Which statement is true regarding component definition in React
```
function SayHi(props) {
 return <h1>Hi, {props.name}</h1>;
}
 class SayHi extends React.Component {

 render() {
 return <h1>Hi, {this.props.name}</h1>;
 }
 
 }
```
Answer:

oO Both codes are equivalent from React's point of view

oO The most simple and concise way to define a component is the first one but classes have some additional features

Oo This funetion is a valid React component because it accepts a single �props� object argument with data and returns a React

� Allof the above
What is true for ReactJS components defined as pure JS functions?

Answer:

oO Pure function components do not have lifecycle methods

oO Itis not possible to set defaultProps or propTypes for pure function components
� Pure function component have not render method defined

oO A pure function is a function that may alter any external state
How set a custom html inside ReactUs component:

Answer:

oO <div innerHTML={'Some custom HTML'}/>

oO <div dangerouslySetInnerHTML={{__html:'Some custom HTML'}}/>
oO <div innerHTML={{__html:'Some custom HTML'}}/>

oO <div dangerouslySetInnerHTML={'Some custom HTML'}/>
Considering the following codes:
```
var MessageBox = React.createClass({
getlnitialState: function() {
return {nmameWithQualifier: 'Mr. ' + this.props.name};
}

render: function() {
return <div>{this.state.nameWithQualifier}</div>;
}
})

ReactDOM.render(<MessageBox name=""Rogers""/>, mountNode);

var MessageBox = React.createClass({
render: function() {
return <div>{'Mr. ' + this. props.name}</div>;
}
})

ReactDOM.render(<MessageBox name=""Rogers"/>, mountNode);

Answer:

O They are both exactly equivalent

O The first one is better than the second one because the second one violates the basic principle of the single source of truth
O The second one is better than the first one because the first one violates the basic principle of the single source of truth

� None of the above
What will happen if parent component will fire render function?

Answer:

� Child components will fire render functions too

oO Child components will fire shouldComponentUpdate
oO Child components will always fire componentDidUpdate

� Child components will fire no event
Considering the following HTML example

 

<a href="#" onclick=""console.log('The link was clicked.');return false>Click me</a>

The same component in React:

Answer:

oO Is the same but with the event on click written in camelCase (i.e. onClick)
oO You must call preventDefault explicitly

� Cannot be built because you cannot return false

� None of the above
Which statement is true regarding state and props in React?

Answer:

� They are not related

oO The state can�t be updated by the parent while props can
oO Both props and state changes trigger a render update

oO The parent's props becomes the child's state value
Which is the correct function to render ReactUS component at server side as static
html page?

Answer:

� ReactDOMServer.renderToString

� ReactDOM.render

� ReactDOM.renderStaticOnServer

� ReactDOMServer.renderToStaticMarkup
 

Which function is invoked just before render during initial render?

Answer:

oO componentWillUpdate()

oO componentBeforeOccur()

oO componentWillReceiveMount()
oO componentWillMount()
Answer:

� Validation

oO getPropsValue

oO Typechecking

oO Both (a) and (c) are correct

PropTypes can be used for...
Which of the following statements is incorrect regarding Flux concept:

Answer:

oO Propose a single directional data flow

oO The reducer is a function that specifies the changes that actions trigger
oO The stores are responsible of re-rendering the app

� The view recieves the data that the dispatcher sends to the stores
Regarding the following code:
import React from 'react';

var newData = {
data: �Data from COMP...�,

var MyCOMP = ComposedComponent ? class extends React. Component {

componentDidMount() {
this.setState({
data: newData.data
yi
}

render(){ .
return <ComposedComponent {...this.props} {...this.state} />;
}
i

class MyComponent extends React.Component {
render() {
return (
<div>
<h1>{this. props data}</h1>
</div>
)
}
}

export default MyYCOMP(MyComponent);

Which statement is false?
The MyCOMP is a higher order function that is used only to pass data to MyComponent

The function MyCOMP takes MyComponent, enhances it with newData and returns the enhanced component that will be rendered
on screen

MyComponent should extends React. PureComponent in order to the code to be correct

If we run the app, we will see "Data from COMP...�
