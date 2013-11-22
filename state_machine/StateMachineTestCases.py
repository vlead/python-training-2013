import StateMachine

"""
 Do we begin with simple cases or complex cases?  
 Are each of the test cases meant to be self contained?  Yes

 Do we throw an exception if the operation was largely successful
 e.g. adding multiple states (one state was empty string)

 Should all the test cases pass?  Ain't some test cases low priority?

"""

if __name__ == "__main__":

    def test_create_state_machine():
        """ Test if state machine is being created? """
        sm1 = StateMachine.StateMachine()

        # This is probably a bad way to do things.
        if hasattr(sm1, "initial_state") and hasattr(sm1, "final_states") and \
           hasattr(sm1, "transitions") and hasattr(sm1, "alphabet") and \
           hasattr(sm1, "states"):
            print "Passed: test_create_state_machine()"
        else:
            print "Failed: test_create_state_machine()"

    def test_add_state_1():
        """ Test if a state can be added """
        sm1 = StateMachine.StateMachine()
        sm1.add_state("  S1 ")
        if "S1" in sm1.states:
            print "Passed: test_add_state_1()"
        else:
            print "Failed: test_add_state_1()"

    def test_add_state_2():
        """ Test if a state can be added """
        sm1 = StateMachine.StateMachine()
        sm1.add_state(1)    # Passing a number instead of a string
        if "1" in sm1.states:
            print "Passed: test_add_state_2()"
        else:
            print "Failed: test_add_state_2()"

    def test_add_invalid_state_1():
        """ Test if a state can be added """
        sm1 = StateMachine.StateMachine()
        try:
            sm1.add_state("   ")
            print "Failed: test_add_invalid_state_1()"
        except InvalidStateException:
            print "Passed: test_add_invalid_state_1()"
        
    def test_add_invalid_state_2():
        """ Test if a state can be added """
        sm1 = StateMachine.StateMachine()
        try:
            sm1.add_state(" !@#$  ")
            print "Failed: test_add_invalid_state_2()"
        except InvalidStateException:
            print "Passed: test_add_invalid_state_2()"

    def test_add_duplicate_state():
        """ DuplicateStateException should occur if state has already been added  """
        sm1 = StateMachine.StateMachine()
        try:
            sm1.add_state("S2")
            sm1.add_state("S2")
            print "Failed: test_add_duplicate_state()"
        except DuplicateStateException:
            print "Passed: test_add_duplicate_state()"

    def test_add_states():
        """ Valid states should be added.  First invalid state should cause
         InvalidStateException """
        sm1 = StateMachine.StateMachine()
        sm1.add_states("S1", "S2", "S3")
        if "S1" in sm1.states and "S2" in sm1.states and "S3" in sm1.states:
            print "Passed: test_add_states()"
        else:
            print "Failed: test_add_states()"

    def test_add_invalid_states():
        """ InvalidStateException should occur if state is blank or whitespace """
        sm1 = StateMachine.StateMachine()
        try:
            sm1.add_states("S1", "", "S3")
            print "Failed: test_add_invalid_states()"
        except InvalidStateException:
            if "S1" in sm1.states:
                print "Passed: test_add_invalid_states()"
            else:
                print "Failed: test_add_invalid_states()"

    def test_remove_existing_state():
        """ Remove if already existing. """
        sm1 = StateMachine.StateMachine()
        sm1.add_states("S1", "S2", "S3")
        sm1.remove_state("S2")
        if "S1" in sm1.states and "S3" in sm1.states and "S2" not in sm1.states:
            print "Passed: test_remove_existing_state()"
        else:
            print "Failed: test_remove_existing_state()"
        pass

    def test_remove_non_existent_state():
        """ NonExistentStateException should occur (don't check for validity) """
        sm1 = StateMachine.StateMachine()
        sm1.add_states("S1", "S2", "S3")
        try:
            sm1.remove_state("S4")
            print "Failed: test_remove_non_existent_state()"
        except NonExistentStateException:
            print "Passed: test_remove_non_existent_state()"

    def test_remove_states():
        """ Remove all existing states until a NonExistentStateException is raised. """
        sm1 = StateMachine.StateMachine()
        sm1.add_states("S1", "S2", "S3")
        sm1.remove_states("S1", "S3")
        if "S1" not in sm1.states and "S3" not in sm1.states and "S2" in sm1.states:
            print "Passed: test_remove_states()"
        else:
            print "Failed: test_remove_states()"

    def test_remove_non_existent_states():
        """ NonExistentStateException should occur if any of the states is blank or
        whitespace.  None"""
        sm1 = StateMachine.StateMachine()
        sm1.add_states("S1", "S2", "S3")
        try:
            sm1.remove_states("S1", "S4")
            print "Failed: test_remove_non_existent_states()"
        except NonExistentStateException:
            if "S1" in sm1.states:
                print "Failed: test_remove_non_existent_states()"
            else:
                print "Passed: test_remove_non_existent_states()"

    def test_set_initial_state_0():
        """ Should allow setting initial state """
        sm1 = StateMachine.StateMachine()
        sm1.add_state("0")
        sm1.set_initial_state("0")
        if sm1.initial_state == "0":
            print "Passed: test_set_initial_state_0()"
        else:
            print "Failed: test_set_initial_state_0()"

    def test_set_initial_state_1():
        """ Should allow setting initial state """
        sm1 = StateMachine.StateMachine()
        sm1.add_state("State1")
        sm1.set_initial_state("State1")
        if sm1.initial_state == "State1":
            print "Passed: test_set_initial_state_1()"
        else:
            print "Failed: test_set_initial_state_1()"

    def test_set_initial_state_2():
        """ Should allow setting initial state """
        sm1 = StateMachine.StateMachine()
        sm1.add_state("2")
        sm1.set_initial_state(" 2   ")
        if sm1.initial_state == "2":
            print "Passed: test_set_initial_state_2()"
        else:
            print "Failed: test_set_initial_state_2()"

    def test_set_initial_state_3():
        """ Should allow setting initial state """
        sm1 = StateMachine.StateMachine()
        sm1.add_state("State1")
        sm1.set_initial_state(" State1   ")
        if sm1.initial_state == "State1":
            print "Passed: test_set_initial_state_3()"
        else:
            print "Failed: test_set_initial_state_3()"

    def test_set_initial_state_4():
        """ Should allow setting initial state """
        sm1 = StateMachine.StateMachine()
        sm1.add_state(1)
        sm1.set_initial_state(1)
        if sm1.initial_state == "1":
            print "Passed: test_set_initial_state_4()"
        else:
            print "Failed: test_set_initial_state_4()"

    def test_set_invalid_initial_state_1():
        """ Should raise an exception """
        sm1 = StateMachine.StateMachine()
        try:
            sm1.set_initial_state("   ")
            print "Failed: test_set_invalid_initial_state_1()"
        except InvalidStateException, NonExistentStateException:  # IS THIS CORRECT?
            print "Passed: test_set_invalid_initial_state_1()"

    def test_set_invalid_initial_state_2():
        """ Should raise an exception """
        sm1 = StateMachine.StateMachine()
        try:
            sm1.set_initial_state(" 1 2  ")
            print "Failed: test_set_invalid_initial_state_2()"
        except InvalidStateException, NonExistentStateException:  # IS THIS CORRECT?
            print "Passed: test_set_invalid_initial_state_2()"

    def test_change_initial_state():
        """ Should set the initial state but also raise exception if initial state already set? """
        sm1 = StateMachine.StateMachine()
        sm1.add_states("S1", "S2")
        sm1.set_initial_state("S1")
        sm1.set_initial_state("S2")
        if "S2" == sm1.initial_state:
            print "Passed: test_change_initial_state()"
        else:
            print "Failed: test_change_initial_state()"

    def test_add_one_final_state():
        """ Should allow setting a final state """
        sm1 = StateMachine.StateMachine()
        sm1.add_states("S1", "S2")
        sm1.add_final_state("S2") ###
        if "S2" in sm1.final_states:
            print "Passed: test_add_one_final_state()"
        else:
            print "Failed: test_add_one_final_state()"

    def test_add_invalid_final_state():
        """ Should raise an exception """
        sm1 = StateMachine.StateMachine()
        try:
            sm1.add_final_state("S2")
            print "Failed: test_add_invalid_final_state()"
        except NonExistentStateException:
            print "Passed: test_add_invalid_final_state()"

    def test_add_multiple_final_states():
        """ Should allow setting multiple final states """
        sm1 = StateMachine.StateMachine()
        sm1.add_states("S1", "S2")
        sm1.add_final_state("S1", "S2")
        if "S1" in sm1.final_states and "S2" in sm1.final_states:
            print "Passed: test_add_multiple_final_states()"
        else:
            print "Failed: test_add_multiple_final_states()"
        pass

    def test_add_multiple_invalid_final_states():
        """ Should add all valid states passed in the parameter before 
        raising an if InvalidStateException state is blank or whitespace """
        sm1 = StateMachine.StateMachine()
        sm1.add_states("S1", "S2")
        try:
            sm1.add_final_state("S1", "S3")
            print "Failed: test_add_multiple_invalid_final_states()"
        except NonExistentStateException:
            if "S1" not in sm1.final_states:
                print "Failed: test_add_multiple_invalid_final_states()"
            else:
                print "Passed: test_add_multiple_invalid_final_states()"

    def test_remove_one_final_state():
        """ Should allow removing a final state """
        sm1 = StateMachine.StateMachine()
        sm1.add_states("S1", "S2")
        sm1.add_final_states("S1", "S2")
        sm1.remove_final_state("S1")
        if "S1" in sm1.final_states and "S1" not in sm1.final_states:
            print "Passed: test_remove_one_final_state()"
        else:
            print "Failed: test_remove_one_final_state()"

    def test_remove_invalid_final_state():
        """ NonExistentStateException should occur """
        sm1 = StateMachine.StateMachine()
        sm1.add_states("S1", "S2")
        try:
            sm1.remove_final_state("S1")
            print "Failed: test_remove_invalid_final_state()"
        except NonExistentStateException:
            print "Passed: test_remove_invalid_final_state()"

    def test_remove_multiple_final_states():
        """ Should allow removing multiple final states """
        sm1 = StateMachine.StateMachine()
        sm1.add_states("S1", "S2")
        sm1.add_final_states("S1", "S2")
        sm1.remove_final_states("S1", "S2")
        if "S1" not in sm1.final_states and \
           "S2" not in sm1.final_states and \
           "S1" in sm1.final_states and \
           "S2" in sm1.final_states:
            print "Passed: test_remove_multiple_final_states()"
        else:
            print "Failed: test_remove_multiple_final_states()"

    def test_remove_invalid_multiple_final_states():
        """ NonExistentStateException should occur """
        sm1 = StateMachine.StateMachine()
        sm1.add_states("S1", "S2")
        try:
            sm1.remove_final_state("S1", "S3")
            print "Failed: test_remove_one_final_state()"
        except NonExistentStateException:
            if "S1" in sm1.states and "S1" not in sm1.final_states:
                print "Passed: test_remove_one_final_state()"
            else:
                print "Failed: test_remove_one_final_state()"

    def test_set_valid_alphabet():
        """  """
        sm1 = StateMachine.StateMachine()
        sm1.set_alphabet("a", "b", "c")

    def test_set_invalid_alphabet():
        pass

    def test_add_valid_symbol():
        pass

    def test_add_invalid_symbol():
        pass

    def test_remove_valid_symbol():
        pass

    def test_remove_non_existent_symbol():
        pass

    try:
        test_create_state_machine()
        test_add_state_1()
        test_add_state_2()
        test_add_invalid_state_1()
        test_add_invalid_state_2()
        test_add_duplicate_state()
        test_add_states()
        test_add_invalid_states()
        test_remove_existing_state()
        test_remove_non_existent_state()
        test_remove_states()
        test_remove_non_existent_states()
        test_set_initial_state_0()
        test_set_initial_state_1()
        test_set_initial_state_2()
        test_set_initial_state_3()
        test_set_initial_state_4()
        test_set_invalid_initial_state_1()
        test_set_invalid_initial_state_2()
        test_change_initial_state()
        test_add_one_final_state()
        test_add_invalid_final_state()
        test_add_multiple_final_states()
        test_add_multiple_invalid_final_states()
        test_remove_one_final_state()
        test_remove_invalid_final_state()
        test_remove_multiple_final_states()
        test_remove_invalid_multiple_final_states()

    except Exception as e:
        print e.message


