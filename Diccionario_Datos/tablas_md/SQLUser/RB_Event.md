# SQLUser.RB_Event

**Schema:** SQLUser
**Columnas:** 41
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**RB Module**. Funcionalidad de módulos Rich Browser.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| EV_RowId | bigint | PK |  | NO | - |
| EV_Administrator_DR | varchar |  | FK | SI | Des Ref CTCP |
| EV_AttendeeFemaleNo | double |  |  | SI | AttendeeFemaleNo |
| EV_AttendeeMaleNo | double |  |  | SI | AttendeeMaleNo |
| EV_AuxInsType_DR | bigint |  | FK | SI | Des Ref AuxInsType |
| EV_Charge | double |  |  | SI | Charge |
| EV_ClientSourceDesc | varchar |  |  | SI | ClientSourceDesc |
| EV_ClientSourceOrg_DR | bigint |  | FK | SI | Client Source Organisation |
| EV_ClientSource_DR | bigint |  | FK | SI | Des Ref ClientSource |
| EV_ClientType | varchar |  |  | SI | ClientType |
| EV_ConsultCategory_DR | bigint |  | FK | SI | Des Ref ConsultCategory |
| EV_ContVenue_DR | bigint |  | FK | SI | Des Ref Patient Contact Venue |
| EV_DateCreated | date |  |  | SI | DateCreated |
| EV_DateFrom | date |  |  | SI | DateFrom |
| EV_DateTo | date |  |  | SI | DateTo |
| EV_Duration | double |  |  | SI | Duration |
| EV_EventSubType_DR | varchar |  | FK | SI | Des Ref EventSubType |
| EV_Hospital_DR | bigint |  | FK | SI | Des Ref CTHospital |
| EV_InsType_DR | bigint |  | FK | SI | Des Ref InsType |
| EV_ItemCat_DR | bigint |  | FK | SI | Des Ref ARCItemCat |
| EV_Location_DR | bigint |  | FK | SI | Des Ref CTLoc |
| EV_MaxNumberOfParticipants | double |  |  | SI | Max Number Of Participants |
| EV_MethodOfConduct_DR | bigint |  | FK | SI | Des Ref Method Of Conduct |
| EV_NFMICategDepart_DR | varchar |  | FK | SI | Des Ref CTNFMICategDepart  |
| EV_Name | varchar |  |  | SI | Name |
| EV_Number | varchar |  |  | SI | Number |
| EV_PredictedReviewTime | time |  |  | SI | Predicted Review Time |
| EV_PredictedTravelTime | time |  |  | SI | Predicted Travel Time |
| EV_PreparationTime | time |  |  | SI | Preparation Time |
| EV_RBResource_DR | bigint |  | FK | SI | Des Ref RBResource |
| EV_Status | varchar |  |  | SI | Status |
| EV_Type_DR | bigint |  | FK | SI | Des Ref Event Type |
| EV_Venue | varchar |  |  | SI | Venue |
| EV_VenueAddress1 | varchar |  |  | SI | Venue Address1 |
| EV_VenueAddress2 | varchar |  |  | SI | Venue Address2 |
| EV_VenueFax | varchar |  |  | SI | Venue Fax |
| EV_VenuePhone | varchar |  |  | SI | Venue Phone |
| EV_YesNo1 | varchar |  |  | SI | YesNo1 |
| EV_YesNo2 | varchar |  |  | SI | YesNo2 |
| EV_YesNo3 | varchar |  |  | SI | YesNo3 |
| EV_YesNo4 | varchar |  |  | SI | YesNo4 |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*