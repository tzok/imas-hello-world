#include <UALClasses.h>
#include <unistd.h>

int main() {
    uid_t uid = geteuid();
    struct passwd *pw = getpwuid(uid);

    IdsNs::IDS ids(1, 1, 0, 0);
    ids.createEnv(pw->pw_name, "test", "3");

    ids._summary.ids_properties.comment = "Hello World from C++";
    ids._summary.ids_properties.homogeneous_time = 1;
    ids._summary.time.resize(1);
    ids._summary.time(0) = 0.1;
    ids._summary.put();

    ids.close();
    return 0;
}
