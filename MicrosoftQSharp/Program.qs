namespace MicrosoftQSharp {
    open Microsoft.Quantum.Intrinsic;
    open Microsoft.Quantum.Canon;
    
    operation SetQubit(desired: Result, target : Qubit): Unit {
      if(desired != M(target)) {
        X(target);
      }
    }

    // Any Q# application must have at least one entry point noted by
    // this attribute, @EntryPoint(). Any input parameters are available
    // as inputs from the console. So our example here to execute would 
    // be in the form of `dotnet run --shots 1000`.
    @EntryPoint()
    operation BellStateExample(shots: Int) : Unit {
        // Like the other examples, we will output the number of
        // times we are in the classical two-bit state 11 and 00
        // Q# (thankfully) has variables as immutable by default,
        // to use mutable variables we must use the mutable key word
        // and use set when mutating the variable
        mutable oneStateCount = 0;
      
        // Q# is drasticaly different from the ibm and aws examples.
        // It is here that quantum computing is treated more as a
        // programmable language, than an SDK generating Quantum
        // assembly code. So, here we must first dynamically
        // allocate two qubits so we can put them into superpositions
        // Notice that we do not use the concept of a Cicuit here.
        // The function definition of operation is the equivalent to
        // a traditional quantum circuit in Q#
        using((q0, q1) = (Qubit(), Qubit())) {
          for(shot in 1..shots) {
            // We need to specify our starting state
            SetQubit(Zero, q0);
            SetQubit(Zero, q1);
            
            // Apply a Hadamard gate to our first qubit
            H(q0);
            // Now apply a Controlled-Not where q0 is the control qubit
            // and q1 is the target qubit
            CNOT(q0, q1);
            
            //There is no easy ascii console circuit printer, so we won't do that in this sample
            
            // Now measure (read the result)
            // Again, this is different from Qiskit and AWS Braket because
            // we are not making a service call to a service exposing a 
            // quantum computer and awaiting a reply, we are measuring immediately
            // Note, we only need to measure the controlling qubit
            if(One == M(q0)) {
              set oneStateCount += 1; 
            }
          }
        }
        
        Message($"'11': {oneStateCount}, '00': {shots - oneStateCount}");
    }
}
