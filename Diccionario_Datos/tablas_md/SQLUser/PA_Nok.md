# SQLUser.PA_Nok

**Schema:** SQLUser
**Columnas:** 180
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| NOK_PAPMI_ParRef | bigint | PK |  | NO | Des Ref to PAPMI |
| NOK_AddrManualEntry | varchar |  |  | SI | Unvalidated address is manually entered |
| NOK_AddreSamID | varchar |  |  | SI | Address eSam ID |
| NOK_Address2 | varchar |  |  | SI | Address2 |
| NOK_CareProfAssocType_DR | bigint |  | FK | SI | Des Ref to PACCareProfAssocType |
| NOK_CareSetting_DR | bigint |  | FK | SI | Des Ref to PACCareSetting |
| NOK_CarerContribution | varchar |  |  | SI | Carer Contribution |
| NOK_ChildSub | numeric |  |  | NO | NOK ChildSub |
| NOK_CityArea_DR | bigint |  | FK | SI | Des Ref CityArea |
| NOK_CityCode_DR | bigint |  | FK | SI | Des Ref CityCode |
| NOK_CityOfBirth_DR | bigint |  | FK | SI | Des Ref to CTCity |
| NOK_CityOfIssue_DR | bigint |  | FK | SI | Des Ref to CTCity |
| NOK_ConsentToShareInfo | varchar |  |  | SI | Consent To Share Info |
| NOK_ContactMethod | varchar |  |  | SI | ContactMethod |
| NOK_ContactType_DR | bigint |  | FK | SI | Des Ref ContactType |
| NOK_CountryOfIssue_DR | bigint |  | FK | SI | Des Ref to CTCountry |
| NOK_Country_DR | bigint |  | FK | SI | Des Ref Country |
| NOK_DateFrom | date |  |  | SI | Date From |
| NOK_DateOfBirth | date |  |  | SI | DateOfBirth |
| NOK_DateTo | date |  |  | SI | Date To |
| NOK_DeceasedFlag | varchar |  |  | SI | DeceasedFlag |
| NOK_DependentLocality | varchar |  |  | SI | DependentLocality |
| NOK_DomicileCode | varchar |  |  | SI | Domicile Code |
| NOK_Email | varchar |  |  | SI | Email |
| NOK_Email2 | varchar |  |  | SI | Email2 |
| NOK_EmailValidationStatus_DR | bigint |  | FK | SI | Des Ref PACEmailValidationStatus |
| NOK_EmploymentStatus_DR | bigint |  | FK | SI | Des Ref to PACEmploymentStatus |
| NOK_ExternalOID | varchar |  |  | SI | ExternalOID |
| NOK_FamilyGroupFlag | varchar |  |  | SI | FamilyGroupFlag |
| NOK_FaxNumber | varchar |  |  | SI | Fax Number |
| NOK_FirstContact | varchar |  |  | SI | First Contact |
| NOK_FirstEnteredBy_DR | bigint |  | FK | SI | Des Ref SSUser |
| NOK_FirstEnteredDate | date |  |  | SI | FirstEnteredDate |
| NOK_FirstEnteredTime | time |  |  | SI | FirstEnteredTime |
| NOK_ForeignAddress | varchar |  |  | SI | Foreign Address |
| NOK_ForeignCity | varchar |  |  | SI | ForeignCity |
| NOK_ForeignPostCode | varchar |  |  | SI | ForeignPostCode |
| NOK_GenderPronounsList | varchar |  |  | SI | List of Gender Pronouns |
| NOK_GenderPronouns_DR | bigint |  | FK | SI | Gender Pronouns - Des Ref to CTGenderPronouns |
| NOK_HouseholdMember | varchar |  |  | SI | Household Member |
| NOK_IDDate | date |  |  | SI | ID Date |
| NOK_IDNo | varchar |  |  | SI | ID No |
| NOK_Inactive | varchar |  |  | SI | Inactive |
| NOK_InactiveReason | varchar |  |  | SI | InactiveReason |
| NOK_IndigenousStatus_DR | bigint |  | FK | SI | Des Ref to PACIndigStatus |
| NOK_MobPhone | varchar |  |  | SI | Mob Phone |
| NOK_Name | varchar |  |  | SI | Name |
| NOK_Name2 | varchar |  |  | SI | Name2 |
| NOK_Name3 | varchar |  |  | SI | Name3 |
| NOK_Name4 | varchar |  |  | SI | Name4 |
| NOK_Nationality_DR | bigint |  | FK | SI | Des Ref to CTNation |
| NOK_NonConsentReason | varchar |  |  | SI | Non Consent Reason |
| NOK_NonGovOrg_DR | bigint |  | FK | SI | Des Ref NonGovOrg |
| NOK_NotValidAddrReason_DR | bigint |  | FK | SI | Not Validated Address Reason - Des Ref to PACNotVa... |
| NOK_Occupation_DR | bigint |  | FK | SI | Des Ref to CTOccupation |
| NOK_OtherPronouns | varchar |  |  | SI | Other Pronouns |
| NOK_PAPER_DR | bigint |  | FK | SI | Des Ref to PAPER |
| NOK_ParentalResponsibility | varchar |  |  | SI | Parental Responsibility |
| NOK_PayorCityBirth_DR | bigint |  | FK | SI | Des Ref City |
| NOK_PostOpContact | varchar |  |  | SI | PostOpContact |
| NOK_PreferredContactMethod | varchar |  |  | SI | PreferredContactMethod |
| NOK_Province_DR | bigint |  | FK | SI | Des Ref Province |
| NOK_Rank | double |  |  | SI | Rank |
| NOK_RcFlag | varchar |  |  | SI | Archived Flag |
| NOK_ReasonForEndDate | varchar |  |  | SI | ReasonForEndDate |
| NOK_ReciprocalContactType_DR | bigint |  | FK | SI | Des Ref ContactType |
| NOK_ReciprocalRelation_DR | bigint |  | FK | SI | Des Ref to CTRLT |
| NOK_Relation_DR | bigint |  | FK | SI | Des Ref to CTRLT |
| NOK_Religion_DR | bigint |  | FK | SI | Des Ref to CTReligion |
| NOK_Remarks | varchar |  |  | SI | Remarks |
| NOK_ResidentMember | varchar |  |  | SI | ResidentMember |
| NOK_RowId | varchar |  |  | NO | - |
| NOK_Sex_DR | bigint |  | FK | SI | Des Ref Sex |
| NOK_StNameLine1 | varchar |  |  | SI | StNameLine1 |
| NOK_TelH | varchar |  |  | SI | TelH |
| NOK_TelO | varchar |  |  | SI | TelO |
| NOK_Title_DR | bigint |  | FK | SI | Des Ref Title_DR |
| NOK_UpdateDate | date |  |  | SI | UpdateDate |
| NOK_UpdateHospital_DR | bigint |  | FK | SI | Des Ref UpdateHospital |
| NOK_UpdateTime | time |  |  | SI | UpdateTime |
| NOK_UpdateUser_DR | bigint |  | FK | SI | Des Ref UpdateUser |
| NOK_Zip_DR | bigint |  | FK | SI | Des Ref Zip |
| Q01 | - |  |  | SI | Nombre Paciente |
| Q02 | - |  |  | SI | Fecha Nacimiento |
| Q03 | - |  |  | SI | RUN |
| Q04 | - |  |  | SI | Fecha Admisión |
| Q05 | - |  |  | SI | Previsión |
| Q06 | - |  |  | SI | Médico Tratante |
| Q07 | - |  |  | SI | Diag Principal Code |
| Q08 | - |  |  | SI | Diag Principal Desc |
| Q09 | - |  |  | SI | Diag Principal Com |
| Q10 | - |  |  | SI | Fecha Hora Prob Alta |
| Q11 | - |  |  | SI | PC Fecha Hora |
| Q12 | - |  |  | SI | PC |
| Q13 | - |  |  | SI | PC User |
| Q14 | - |  |  | SI | Alergias |
| Q15 | - |  |  | SI | Dias Hosp |
| Q16 | - |  |  | SI | RC Fecha Hora |
| Q17 | - |  |  | SI | RC |
| Q18 | - |  |  | SI | RC User |
| Q19 | - |  |  | SI | ERD Fecha Hora |
| Q20 | - |  |  | SI | ERD |
| Q21 | - |  |  | SI | ERD User |
| Q22 | - |  |  | SI | ERDSM Fecha Hora |
| Q23 | - |  |  | SI | ERDSM |
| Q24 | - |  |  | SI | ERDSM User |
| Q25 | - |  |  | SI | Regimen Fecha Hora |
| Q26 | - |  |  | SI | Regimen |
| Q27 | - |  |  | SI | Regimen User |
| Q28 | - |  |  | SI | NC Fecha Hora |
| Q29 | - |  |  | SI | NC |
| Q30 | - |  |  | SI | NC User |
| Q31 | - |  |  | SI | CAF Fecha Hora |
| Q32 | - |  |  | SI | CAF |
| Q33 | - |  |  | SI | CAF User |
| Q34 | - |  |  | SI | PT Fecha Hora |
| Q35 | - |  |  | SI | PT Peso |
| Q36 | - |  |  | SI | PT Talla |
| Q37 | - |  |  | SI | PT User |
| Q38 | - |  |  | SI | OT Fecha User |
| Q39 | - |  |  | SI | OT |
| Q40 | - |  |  | SI | OT User |
| Q41 | - |  |  | SI | BS Fecha Hora |
| Q42 | - |  |  | SI | BS |
| Q43 | - |  |  | SI | BS User |
| Q44 | - |  |  | SI | Alias |
| Q45 | - |  |  | SI | Hora Admision |
| Q46 | - |  |  | SI | Nro Pasaporte |
| Q47 | - |  |  | SI | Nro Registro |
| Q48 | - |  |  | SI | UC Dias |
| Q49 | - |  |  | SI | UC |
| Q50 | - |  |  | SI | Tipo Entrega |
| Q51 | - |  |  | SI | CF Fecha Hora |
| Q52 | - |  |  | SI | CF |
| Q53 | - |  |  | SI | CF User |
| Q54 | - |  |  | SI | RLPP Fecha |
| Q55 | - |  |  | SI | RLPP |
| Q56 | - |  |  | SI | RLPP User |
| Q57 | - |  |  | SI | Ubicación |
| Q58 | - |  |  | SI | Médico de Turno |
| QUESAnaDR | - |  |  | SI | Anaesthesia |
| QUESAnaOperationDR | - |  |  | SI | Operation |
| QUESConsultDR | - |  |  | SI | Consult |
| QUESCopiedComments | - |  |  | SI | Copied Comments |
| QUESCopiedDate | - |  |  | SI | Copied Date |
| QUESCopiedEpDR | - |  |  | SI | Copied Episode |
| QUESCopiedSourceDR | - |  |  | SI | Copied Source DR |
| QUESCopiedTime | - |  |  | SI | Copied Time |
| QUESCopiedUserDR | - |  |  | SI | Copied User |
| QUESCreateDate | - |  |  | SI | Creation Date |
| QUESCreateTime | - |  |  | SI | Creation Time |
| QUESCreateUserDR | - |  |  | SI | Creation User |
| QUESDate | - |  |  | SI | Last Update Date |
| QUESErrorReasonDR | - |  |  | SI | Error Reason |
| QUESFHResidentDR | - |  |  | SI | Resident |
| QUESMRClinicalPathWaysDR | - |  |  | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | - |  |  | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | - |  |  | SI | Order Execution |
| QUESORPreanaestheticConsultDR | - |  |  | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | - |  |  | SI | Observation Entry |
| QUESOperRoomDR | - |  |  | SI | Operating Room |
| QUESPAAdmDR | - |  |  | SI | Admission |
| QUESPAAdverseEventDR | - |  |  | SI | Adverse Event |
| QUESPAPatMasDR | - |  |  | SI | Patient |
| QUESPAPregnancyDR | - |  |  | SI | Pregnancy |
| QUESPAWaitingListDR | - |  |  | SI | Waiting List |
| QUESPathwayItemDR | - |  |  | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | - |  |  | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | - |  |  | SI | Appointments |
| QUESRBApptOutcomeDR | - |  |  | SI | Appointment Outcome |
| QUESRBApptSlotDR | - |  |  | SI | Appointment Slot |
| QUESReasonForCorrectionDR | - |  |  | SI | Reason for Correction |
| QUESSSUserDefWindowDR | - |  |  | SI | Questionnaire |
| QUESScore | - |  |  | SI | Score |
| QUESSecondUserDR | - |  |  | SI | Second Signature |
| QUESStatusDR | - |  |  | SI | Status |
| QUESTextResultDR | - |  |  | SI | Text Result |
| QUESTime | - |  |  | SI | Last Update Time |
| QUESTransactionDR | - |  |  | SI | Transaction |
| QUESUserDR | - |  |  | SI | Last Update User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*