program test
    use ids_routines

    integer :: pulsectx, status;
    type(ids_summary) :: summary;

    call ual_begin_pulse_action(MDSPLUS_BACKEND, 1, 1, 'imas', 'test', '3', pulsectx)
    call ual_open_pulse(pulsectx, FORCE_CREATE_PULSE, '', status);

    allocate(summary%ids_properties%comment(1))
    summary%ids_properties%comment(1) = 'Hello World from Fortran'
    summary%ids_properties%homogeneous_time = 1;
    allocate(summary%time(1))
    summary%time(1) = 0.1

    call ids_put(pulsectx, "summary", summary)
    call ids_deallocate(summary)
    call ual_close_pulse(pulsectx, FORCE_CREATE_PULSE, '', status)
end program test
