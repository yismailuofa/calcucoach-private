import StartButton from "./StartButton";
import { CSSTransition } from "react-transition-group";
import "./styles/slideX.css";
import { useRef } from "react";

export default function StartText({ nextStep, step, isFaq }) {
  const nodeRef = useRef(null)
  return (
    <CSSTransition
      in={step === 0 && !isFaq}
      timeout={1400}
      classNames="slideX"
      unmountOnExit={true}
      nodeRef={nodeRef}
    >
      <div
        style={{
          fontSize: "5vh",
          background:
            "linear-gradient(180deg, rgba(74,134,186,1) 50%, rgba(51,96,136,1) 100%)",
          padding: "4vh",
          paddingTop: "2vh",
          marginTop: "-4vh",
          borderRadius: "4vh",
          display: "flex",
          flexDirection: "column",
          position: "relative",
          justifyText: "center",
          boxShadow: "0vw 5px 20px black",
        }}
        ref={nodeRef}
      >
        Free training.
        <br />
        Made for you.
        <StartButton nextStep={nextStep} />
      </div>
    </CSSTransition>
  );
}
