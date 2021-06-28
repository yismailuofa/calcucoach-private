import { useRef, useState } from "react";
import { CSSTransition } from "react-transition-group";
import MaleButton from "./MaleButton";
import FemaleButton from "./FemaleButton";
import BackButton from "./BackButton";
import "./styles/slideX.css";

export default function GenderText({
  nextStep,
  prevStep,
  setGender,
  step,
  isFaq,
}) {
  const [animationDirection, setanimationDirection] = useState("slideXmiddle");
  const nodeRef = useRef(null);

  const handleBack = () => {
    setanimationDirection("slideXfront");
    prevStep();
  };

  const handleChoice = (gender) => {
    setGender(gender);
    nextStep();
  };

  return (
    <CSSTransition
      in={step === 1 && !isFaq}
      timeout={900}
      classNames={animationDirection}
      unmountOnExit={true}
      nodeRef={nodeRef}
      onExited={() =>
        animationDirection === "slideXmiddle" &&
        setanimationDirection("slideXbehind")
      }
      onEntered={() => setanimationDirection("slideXmiddle")}
    >
      <div
        style={{
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
        }}
        ref={nodeRef}
      >
        <div
          style={{
            fontSize: "4vh",
            background:
              "linear-gradient(180deg, rgba(74,134,186,1) 50%, rgba(51,96,136,1) 100%)",
            padding: "4vh",
            marginTop: "2vh",
            borderRadius: "4vh",
            justifyText: "center",
            boxShadow: "0vw 5px 20px black",
          }}
        >
          What is your gender?
          <div
            style={{
              display: "flex",
              justifyContent: "space-around",
              marginBottom: "1vh",
            }}
          >
            <MaleButton onClick={() => handleChoice("male")}/>
            <FemaleButton onClick={() => handleChoice("female")}/>
          </div>
        </div>
        <BackButton onClick={handleBack} />
      </div>
    </CSSTransition>
  );
}
