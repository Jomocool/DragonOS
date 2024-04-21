use core::sync::atomic::AtomicUsize;

int_like!(Uid, AtomicUid, usize, AtomicUsize);
int_like!(Gid, AtomicGid, usize, AtomicUsize);

#[derive(Debug, Clone)]
pub struct Cred {
    uid: Uid,
    gid: Gid,
    suid: Uid,
    sgid: Gid,
    euid: Uid,
    egid: Gid,
}

impl Cred {
    pub fn idle_cred() -> Self {
        Self {
            uid: Uid(0),
            gid: Gid(0),
            suid: Uid(0),
            sgid: Gid(0),
            euid: Uid(0),
            egid: Gid(0),
        }
    }

    pub fn uid(&self) -> Uid {
        self.uid
    }

    pub fn gid(&self) -> Gid {
        self.gid
    }

    pub fn suid(&self) -> Uid {
        self.suid
    }

    pub fn sgid(&self) -> Gid {
        self.sgid
    }

    pub fn euid(&self) -> Uid {
        self.euid
    }

    pub fn egid(&self) -> Gid {
        self.egid
    }

    pub fn setuid(&mut self, uid: Uid) {
        self.uid = uid;
    }

    pub fn setgid(&mut self, gid: Gid) {
        self.gid = gid;
    }
}
