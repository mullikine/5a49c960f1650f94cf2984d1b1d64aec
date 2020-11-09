# System Architecture: User -> Auth Server -> ctx -> service.method(ctx, params…)
# Design contents are immutable after created
# DesignService.methods(ctx,.......)

# service = DesignService()
# foo_id = service.create_design(ctx, 'foo')
# service.get_design(ctx, foo_id) -> 'foo'


from typing import List, Iterable
import uuid


# Identifies the caller of a service method.
class AuthContext:
    def __init__(self, user_id: str):
        self.user_id = user_id  # E.g. ‘userAbc’

# Any calls made to this service are authenticated.
class DesignServiceInterface:
    def create_design(self, ctx: AuthContext, design_content: str) -> str:
        """Creates a design and returns the design id"""
        raise NotImplementedError

    def get_design(self, ctx: AuthContext, design_id: str) -> str:
        """Returns the design content, if the user has access to the design."""
        raise NotImplementedError

class DesignService(DesignServiceInterface):
    def __init__(self):
        # {user id -> (design ids)}
        self.userdidmap = {}

        # {design_id -> content}
        self.didcontentmap = {}

    def create_design(self, ctx: AuthContext, design_content: str) -> str:
        """Creates a design and returns the design id"""

        if self.userdidmap[ctx.user_id]:
            newid = uuid.uuid4()
            self.userdidmap[ctx.user_id].append(str(newid))

        # Get the did then set
        self.didcontentmap[newid] = design_content

        return str(newid)

    def get_design(self, ctx: AuthContext, design_id: str) -> str:
        """Returns the design content, if the user has access to the design."""

        return self.usercontentdict.get(ctx.user_id)

def main():
    service = DesignService()

    foo_id = service.create_design(ctx, 'foo')
    service.get_design(ctx, foo_id) -> 'foo'