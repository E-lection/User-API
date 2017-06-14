from django.http import JsonResponse, HttpResponse, HttpResponseForbidden

UNAUTHORIZED_CODE = 401

STATION_KEY = 'uYx%mfq;XglNP^G1OSKv/]z=!S!K*y'
BOOTH_KEY = '*qGf_P$@mokuQhOaV1^q5}*WfX]3FU'
VOTER_KEY = '8Pqv^>#aU68x(Lcg$e>Oz++@/\"UJ.~'
RESULTS_KEY = 'XMEtV5S]"Bok-<{W4\'2g7h7}>kkjfy'
PINS_KEY = ';]u->is/1r]VrzL4v.HuT/@}>>@95_'
OUTCOME_KEY = 'Mk~@9e{xTM3k11(SW-C|VUeB_.aijg'


def verify(verif):
    def perform(func):
        def inner(request, **kwargs):
            # Does the user have an API key? (should also check they key is valid)
            if 'Authorization' in request.META:
                # Does the user have appropriate permissions?
                if verif()(request.META['Authorization']):
                    return func(request, **kwargs)
                return HttpResponseForbidden()
            return HttpResponse(status=UNAUTHORIZED_CODE)
        return inner
    return perform


def is_station(key):
    return key == STATION_KEY


def is_booth(key):
    return key == BOOTH_KEY


def is_voter(key):
    return key == VOTER_KEY


def is_results(key):
    return key == RESULTS_KEY


def is_pins(key):
    return key == PINS_KEY


def is_outcome(key):
    return key == OUTCOME_KEY


def has_set_voter_has_active_pin_permissions(key):
    # Do some magic stuff to verify the API key
    return False


def has_check_votable_permissions(key):
    # Do some magic stuff to verify the API key
    return False


def has_get_voters_permissions(key):
    # Do some magic stuff to verify the API key
    return False


def has_make_voter_ineligible_permissions(key):
    # Do some magic stuff to verify the API key
    return False


def has_get_candidates_permissions(key):
    # Do some magic stuff to verify the API key
    return False
