export default function FaqText() {
  return (
    <div
      style={{
        fontSize: "3vh",
        width: "80vw",
        maxHeight: "55vh",
        background: "linear-gradient(180deg, rgba(74,134,186,1) 50%, rgba(51,96,136,1) 100%)",
        padding: "4vh",
        borderRadius: "4vh",
        display: "flex",
        flexDirection: "column",
        position: "relative",
        justifyText: "center",
        boxShadow: "0vw 5px 20px black",
        overflow: "auto",
      }}
    >
      Q: What does A x B mean?
      <br />
      <div style={{ fontSize: "2.5vh" }}>
        A: This notation means A sets of B reps. This means you do the exercise
        A times and repeat the motion within the exercise B times.
      </div>
      <br />
      Q: How do I do this exercise?
      <br />
      <div style={{ fontSize: "2.5vh" }}>
        A: All the exercises are designed to be easily found with a Google
        Search. We are working on developing training videos for you to follow
        along with.
      </div>
      <br />
      Q: How long do these workouts take?
      <br />
      <div style={{ fontSize: "2.5vh" }}>
        A: These workouts are designed to take about 1 hour in the gym. This
        depends on things such as experience level and rest time.
      </div>
      <br />
      Q: When will I see results?
      <br />
      <div style={{ fontSize: "2.5vh" }}>
        A: This is a tough question because results depend on a number of factors such as 
    diet, exeperience, intensity, form, and many more. A general estimate is that you
    can see results within 3 months.
      </div>
      {/* <br /> */}
    </div>
  );
}
