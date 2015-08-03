"""
Data layer serialization operations.  Converts querysets to simple
python containers (mainly arrays and dicts).
"""
from . import models


def serialize_organization(organization):
    """
    Organization object-to-dict serialization
    """
    return {
        'id': organization.id,
        'name': organization.name,
        'description': organization.description,
        'logo': organization.logo
    }


def serialize_organization_with_course(organization_course):
    """
    OrganizationCourse serialization (composite object)
    """
    return {
        'id': organization_course.organization.id,
        'name': organization_course.organization.name,
        'description': organization_course.organization.description,
        'logo': organization_course.organization.logo,
        'course_id': organization_course.course_id
    }


def serialize_organizations(organizations):
    """
    Organization serialization
    Converts list of objects to list of dicts
    """
    return [serialize_organization(organization) for organization in organizations]


def deserialize_organization(organization_dict):
    """
    Organization dict-to-object serialization
    """
    return models.Organization(
        id=organization_dict.get('id'),
        name=organization_dict.get('name', ''),
        description=organization_dict.get('description', ''),
        logo=organization_dict.get('logo', '')
    )
