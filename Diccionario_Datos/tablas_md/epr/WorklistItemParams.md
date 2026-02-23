# epr.WorklistItemParams

**Schema:** epr
**Columnas:** 71
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| WIPARCIMDR | varchar |  | FK | SI | - |
| WIPAccessionNo | varchar |  |  | SI | - |
| WIPAdmType | varchar |  |  | SI | - |
| WIPAttendeeOutcome | varchar |  |  | SI | ez log 63423 22/03/2011 $$ delimited string of (ou... |
| WIPCPList | varchar |  |  | SI | CTCareProv |
| WIPCSWorklistParams | varchar |  |  | SI | - |
| WIPCareProvDR | varchar |  | FK | SI | - |
| WIPCaseManager | varchar |  |  | SI | - |
| WIPClinicListType | varchar |  |  | SI | - |
| WIPCode | varchar |  |  | SI | ab 4.03.09 71251 - used by xml import/export |
| WIPDateFrom | date |  |  | SI | - |
| WIPDateFromToday | bit |  |  | SI | - |
| WIPDateTo | date |  |  | SI | - |
| WIPDateToToday | bit |  |  | SI | - |
| WIPDiaryType | varchar |  |  | SI | Standard Type - Diary Type |
| WIPDtFromOffset | varchar |  |  | SI | - |
| WIPDtToOffset | varchar |  |  | SI | - |
| WIPEQDR | bigint |  | FK | SI | - |
| WIPEpisodeTypeList | varchar |  |  | SI | Standard Type - Episode Type |
| WIPEventStatus | varchar |  |  | SI | $$ delimited string of (event status*show) for car... |
| WIPHospitalDR | bigint |  | FK | SI | - |
| WIPHospitalList | varchar |  |  | SI | CTHospital |
| WIPInpatAdmTypeDR | bigint |  | FK | SI | - |
| WIPInqReqStatus | varchar |  |  | SI | $$ delimited string of (referral status*show) for ... |
| WIPLocList | varchar |  |  | SI | CTLoc |
| WIPLocationDR | bigint |  | FK | SI | - |
| WIPLogonCP | bit |  |  | SI | - |
| WIPLogonCareProvRR | bit |  |  | SI | - |
| WIPLogonCaseMan | bit |  |  | SI | - |
| WIPLogonHosp | bit |  |  | SI | - |
| WIPLogonLoc | bit |  |  | SI | - |
| WIPLogonSpecialty | bit |  |  | SI | - |
| WIPNoAppts | bit |  |  | SI | - |
| WIPNurseTabList | varchar |  |  | SI | - |
| WIPOnlyEpsInCompleteDS | bit |  |  | SI | - |
| WIPOnlyEpsOutstandingDS | bit |  |  | SI | - |
| WIPOrderCatList | varchar |  |  | SI | OECOrderCategory |
| WIPOrderStatus | varchar |  |  | SI | OECOrderStatus |
| WIPOrderSubCatList | varchar |  |  | SI | ARCItemCat |
| WIPOutpatLoc | bit |  |  | SI | - |
| WIPPatientNo | varchar |  |  | SI | - |
| WIPRESDesc | varchar |  |  | SI | - |
| WIPRadStatus | varchar |  |  | SI | StandardType "RadiologyOrderStatus" |
| WIPReceivingLoc | varchar |  |  | SI | CTLoc |
| WIPRefResourceList | varchar |  |  | SI | RBResource |
| WIPRefSUBTList | varchar |  |  | SI | PACEpisodeSubType |
| WIPReferralStatus | varchar |  |  | SI | $$ delimited string of (referral status*show) for ... |
| WIPRemoveOrderOffBooking | bit |  |  | SI | - |
| WIPRemovePtOffBooking | bit |  |  | SI | - |
| WIPResourceDR | bigint |  | FK | SI | - |
| WIPResultStatus | varchar |  |  | SI | Standard Type - Result Type |
| WIPSharedCP | bit |  |  | SI | Include Shared Care Patients |
| WIPSortDirection | varchar |  |  | SI | StandardType COLUMNSortOrder |
| WIPSortOrder | varchar |  |  | SI | $$ delimited string of (referral status*show) for ... |
| WIPSpecialtyList | varchar |  |  | SI | CTLoc |
| WIPStatusList | varchar |  |  | SI | OECOrderStatus |
| WIPSubCategoryList | varchar |  |  | SI | ARCItemCat |
| WIPUnitList | varchar |  |  | SI | CTLoc |
| WIPViewAdm | bit |  |  | SI | - |
| WIPViewAll | bit |  |  | SI | - |
| WIPViewDisch | bit |  |  | SI | - |
| WIPViewPread | bit |  |  | SI | - |
| WIPVisitNo | varchar |  |  | SI | - |
| WIPVisitStatus | varchar |  |  | SI | StandardType - AdmStatus |
| WIPWLI | varchar |  |  | SI | Deprecated. Not used. |
| WIPWardList | varchar |  |  | SI | PACWard |
| WIPWorklistItemDefDR | bigint |  | FK | SI | - |
| WIP_Owner | varchar |  |  | SI | Owner - Standard type "EditionOwnerType" |
| WIPdtDischargeFromOffset | varchar |  |  | SI | Discharge Date From Offset |
| WIPdtDischargeToOffset | varchar |  |  | SI | Discharge Date To Offset |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*