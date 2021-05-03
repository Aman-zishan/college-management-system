from django import template

register = template.Library()


@register.filter
def sub_notes(notes, subject_id):
    return notes.filter(subject_id=subject_id)


@register.filter
def sub_qp(qps, subject_id):
    return qps.filter(subject_id=subject_id)


@register.filter
def sub_assignment(assignment, subject_id):
    return assignment.filter(subject_id=subject_id)



