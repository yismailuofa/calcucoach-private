import banner from "../assets/banner.jpg";
import bannerBlurred from "../assets/bannerBlurred.jpg";
import StartText from "./StartText";
import FaqText from "./FaqText";
import FaqBack from "./FaqBack";
import { Component } from "react";

export default class Jumbotron extends Component {
  constructor(props) {
    super(props);
    this.state = {
      step: 0,
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

  render() {
    const bannerImg = this.props.isFaq ? bannerBlurred : banner;
    return (
      <div
        style={{
          backgroundImage: `url(${bannerImg})`,
          width: "100vw",
          height: "100vh",
          backgroundSize: "cover",
          backgroundPosition: "45% 55%",
          display: "flex",
          flexDirection: "column",
          justifyContent: "center",
          alignItems: "center",
          transition: "background-image .7s linear",
        }}
      >
        {this.props.isFaq && (
          <>
            <FaqText /> <FaqBack faqHide={this.props.faqHide} />
          </>
        )}

        {!this.props.isFaq && this.state.step === 0 && (
          <StartText nextStep={this.nextStep} />
        )}
      </div>
    );
  }
}
