# System Architecture: User -> Auth Server -> ctx -> service.method(ctx, params…)
# Design contents are immutable after created
# DesignService.methods(ctx,.......)

# service = DesignService()
# foo_id = service.create_design(ctx, 'foo')
# service.get_design(ctx, foo_id) -> 'foo'


from typing import List, Iterable

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

class DesignServiceInterfaceSomething(DesignServiceInterface):
    def __init__(self):
        self.usercontentdict = {}

    def create_design(self, ctx: AuthContext, design_content: str) -> str:
        """Creates a design and returns the design id"""

        self.usercontentdict[ctx.user_id] = design_content

    def get_design(self, ctx: AuthContext, design_id: str) -> str:
        """Returns the design content, if the user has access to the design."""

        return self.usercontentdict[ctx.user_id]