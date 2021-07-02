import banner from "../assets/banner.jpg";
import StartText from "./StartText";
import FaqScreen from "./FaqScreen";
import GenderText from "./GenderText";
import WorkoutStyles from "./WorkoutStyles";
import WorkoutInfo from "./WorkoutInfo";
import WorkoutDays from "./WorkoutDays";
import { Component } from "react";

export default class Jumbotron extends Component {
  constructor(props) {
    super(props);
    this.state = {
      step: 0,
      gender: "male",
      workoutStyle: 0,
      workoutDays: 3,
      isWorkoutInfo: false,
    };
  }

  prevStep = (e) => {
    this.setState({
      step: this.state.step - 1,
    });
  };

  nextStep = (e) => {
    this.setState({
      step: this.state.step + 1,
    });
  };

  setGender = (gender) => {
    this.setState({
      gender: gender,
    });
  };

  setStyle = (style) => {
    this.setState({
      workoutStyle: style,
    });
  };

  workoutInfoHide = (e) => {
    this.setState({
      isWorkoutInfo: false,
    });
  };

  workoutInfoShow = (e) => {
    this.setState({
      isWorkoutInfo: true,
    });
  };

  setDay = (day) => {
    this.setState({
      workoutDays: day,
    });
  };

  render() {
    return (
      <div
        style={{
          backgroundImage: `url(${banner})`,
          width: "100vw",
          height: "100vh",
          backgroundSize: "cover",
          backgroundPosition: "45% 42%",
          display: "flex",
          flexDirection: "column",
          justifyContent: "center",
          alignItems: "center",
        }}
      >
        <FaqScreen faqHide={this.props.faqHide} isFaq={this.props.isFaq} />
        <StartText
          nextStep={this.nextStep}
          step={this.state.step}
          isFaq={this.props.isFaq}
        />
        <GenderText
          nextStep={this.nextStep}
          prevStep={this.prevStep}
          setGender={this.setGender}
          step={this.state.step}
          isFaq={this.props.isFaq}
        />
        <WorkoutStyles
          nextStep={this.nextStep}
          prevStep={this.prevStep}
          setStyle={this.setStyle}
          step={this.state.step}
          isFaq={this.props.isFaq}
          gender={this.state.gender}
          isWorkoutInfo={this.state.isWorkoutInfo}
          workoutInfoShow={this.workoutInfoShow}
        />
        <WorkoutInfo
          isWorkoutInfo={this.state.isWorkoutInfo}
          isFaq={this.props.isFaq}
          workoutInfoHide={this.workoutInfoHide}
        />
        <WorkoutDays
          nextStep={this.nextStep}
          prevStep={this.prevStep}
          setDay={this.setDay}
          step={this.state.step}
          isFaq={this.props.isFaq}
        />
      </div>
    );
  }
}
