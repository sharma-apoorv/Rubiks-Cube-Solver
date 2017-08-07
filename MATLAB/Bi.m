function [a] = Bi(x)
    a = x;
    % Face Rotation
    a(6,1) = x(4,1);
    a(5,1) = x(4,2);
    a(4,1) = x(4,3);
    a(6,2) = x(5,1);
    a(4,2) = x(5,3);
    a(6,3) = x(6,1);
    a(5,3) = x(6,2);
    a(4,3) = x(6,3);
    % Side Rotation
    a(6,12) = x(1,9);
    a(5,12) = x(1,8);
    a(4,12) = x(1,7);
    a(1,9) = x(4,4);
    a(1,8) = x(5,4);
    a(1,7) = x(6,4);
    a(6,4) = x(9,9);
    a(5,4) = x(9,8);
    a(4,4) = x(9,7);
    a(9,9) = x(4,12);
    a(9,8) = x(5,12);
    a(9,7) = x(6,12);



end