# SQLUser.PA_SMRExtract

**Schema:** SQLUser
**Columnas:** 86
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Extensión de datos adicionales.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SMRE_RowId | bigint | PK |  | NO | - |
| SMRE_AdmissionDate | date |  |  | SI | Admission Date |
| SMRE_AdmissionReason_DR | bigint |  | FK | SI | Des Ref AdmissionReason |
| SMRE_AdmissionTransferred | bigint |  |  | SI | Des Ref Admission Transferred(ref clinic) |
| SMRE_AdmissionType | varchar |  |  | SI | AdmissionType |
| SMRE_AppointmentTime | time |  |  | SI | Appointment Time |
| SMRE_AttendanceClass | varchar |  |  | SI | Attendance Class |
| SMRE_AttendanceFollow_up | varchar |  |  | SI | Attendance Follow up |
| SMRE_AttendanceStatus | varchar |  |  | SI | Attendance Status |
| SMRE_Batch_DR | bigint |  | FK | SI | Des Ref SMR Batch |
| SMRE_BedTransferReason_DR | bigint |  | FK | SI | Des Ref Bed Transfer Reason |
| SMRE_Bedlent_from_speciality | varchar |  |  | SI | Bed lent_from_speciality |
| SMRE_BorrowedBedindicator | varchar |  |  | SI | Borrowed Bed indicator |
| SMRE_ClinicCode | varchar |  |  | SI | Clinic Code |
| SMRE_ClinicDate | date |  |  | SI | Clinic Date |
| SMRE_ClinicTime | time |  |  | SI | Clinic Time |
| SMRE_ClinicianResponsibleOther_DR | varchar |  | FK | SI | Des Ref ClinicianResponsibleOther |
| SMRE_ClinicianResponsible_DR | varchar |  | FK | SI | Des Ref ClinicianResponsible |
| SMRE_CommunityHealthIndex | varchar |  |  | SI | Community Health Index |
| SMRE_ContrIdProviderCode | varchar |  |  | SI | Contr Id Provider Code |
| SMRE_ContractIdentifierContNo | varchar |  |  | SI | Contract Identifier Cont No |
| SMRE_ContractIdentifierPurchaser | varchar |  |  | SI | ContractIdentifierPurchaser |
| SMRE_DateOfBirth | date |  |  | SI | Date Of Birth |
| SMRE_DateofProcedure | date |  |  | SI | Date of Procedure |
| SMRE_DateofProcedures | varchar |  |  | SI | Date of Procedures |
| SMRE_Day_case_suit_indicator | varchar |  |  | SI | Day_case_suit_indicator |
| SMRE_DetailsofOSinterview | varchar |  |  | SI | Details of OS interview |
| SMRE_DischargeDate | date |  |  | SI | Discharge Date |
| SMRE_DischargeDestination | varchar |  |  | SI | DischargeDestination |
| SMRE_DischargeDestination_DR | bigint |  | FK | SI | Des Ref DischargeDestination |
| SMRE_DischargeType | varchar |  |  | SI | DischargeType |
| SMRE_DischargeType_DR | bigint |  | FK | SI | Des Ref Discharge Type |
| SMRE_EthnicGroup_DR | bigint |  | FK | SI | Des Ref EthnicGroup |
| SMRE_ExpectedLOS | varchar |  |  | SI | Expected LOS |
| SMRE_ExtractBuild_DR | bigint |  | FK | SI | Des Ref ExtractBuild |
| SMRE_ExtractNumber | double |  |  | SI | ExtractNumber |
| SMRE_FirstForename | varchar |  |  | SI | First Forename |
| SMRE_GPCode_DR | varchar |  | FK | SI | Des Ref GP Code |
| SMRE_GPreferralletternumber | varchar |  |  | SI | GP referral letter number |
| SMRE_HospitalChaplainVisitRequired | varchar |  |  | SI | Hospital Chaplain Visit Required |
| SMRE_HospitalPatientIdent | varchar |  |  | SI | Hospital Patient Identifier |
| SMRE_InvalidIndicator | varchar |  |  | SI | Invalid Indicator |
| SMRE_LocationHospital_DR | bigint |  | FK | SI | Location/Hospital |
| SMRE_MainProcedure | varchar |  |  | SI | Main Procedure |
| SMRE_Managementofpatient | varchar |  |  | SI | Management of patient |
| SMRE_Marital_DR | bigint |  | FK | SI | Des Ref Marital |
| SMRE_NHSNumber | varchar |  |  | SI | NHS Number |
| SMRE_OSVStatus | varchar |  |  | SI | OSV Status |
| SMRE_OtherDiagnosis | varchar |  |  | SI | Other Diagnosis |
| SMRE_Otherprocedures | varchar |  |  | SI | Other procedures |
| SMRE_Own_minister_indicator | varchar |  |  | SI | Own_minister_indicator |
| SMRE_PASMR_DR | bigint |  | FK | SI | Des Ref PASMR |
| SMRE_PatientAddress | varchar |  |  | SI | Patient Address |
| SMRE_PatientCategory | varchar |  |  | SI | Patient Category |
| SMRE_PreviousSurname | varchar |  |  | SI | Previous Surname |
| SMRE_Prime_diagnosis_conditi | varchar |  |  | SI | Prime_diagnosis condition |
| SMRE_Primeprocedure | varchar |  |  | SI | Prime procedure |
| SMRE_ReadyforDischargedate | date |  |  | SI | Ready for Discharge date |
| SMRE_Reasonfordelayindisc | varchar |  |  | SI | Reason for delay in discharge |
| SMRE_RecordType | varchar |  |  | SI | Record Type |
| SMRE_RefClinc_DR | bigint |  | FK | SI | Des Ref RefClinc |
| SMRE_ReferralReason1 | varchar |  |  | SI | Referral Reason1 |
| SMRE_ReferralReason2 | varchar |  |  | SI | Referral Reason2 |
| SMRE_ReferralReceivedDate | date |  |  | SI | Referral Received Date |
| SMRE_ReferralSource_DR | bigint |  | FK | SI | Des Ref ReferralSource |
| SMRE_ReferralType | varchar |  |  | SI | Referral Type |
| SMRE_Referrercode | varchar |  |  | SI | Referrercode |
| SMRE_ResponsibleHCP_DR | varchar |  | FK | SI | Des Ref ResponsibleHCP |
| SMRE_SecondForename | varchar |  |  | SI | Second Forename |
| SMRE_Sex_DR | bigint |  | FK | SI | Des Ref Sex |
| SMRE_SignificantFacility_DR | bigint |  | FK | SI | Des Ref Significant Facility |
| SMRE_SourceOfAdmission | varchar |  |  | SI | SourceOfAdmission |
| SMRE_SourceofAdmission_DR | bigint |  | FK | SI | Des Ref Source of Admission |
| SMRE_Speciality | varchar |  |  | SI | Speciality |
| SMRE_SpellCarePackageid | varchar |  |  | SI | Spell Care Package id |
| SMRE_StatisticsIndicator | varchar |  |  | SI | Statistics Indicator |
| SMRE_Surname | varchar |  |  | SI | Surname |
| SMRE_TimePatientseen | time |  |  | SI | Time Patient seen |
| SMRE_TimeofArrival | time |  |  | SI | Time of Arrival |
| SMRE_TimeofDeparture | time |  |  | SI | Time of Departure |
| SMRE_WLGuarantExcCode_DR | bigint |  | FK | SI | Des Ref WLGuarantExcCode |
| SMRE_WaitList_DR | bigint |  | FK | SI | Des Ref WaitList |
| SMRE_WaitingListDate | date |  |  | SI | Waiting List Date |
| SMRE_WaitingListType | varchar |  |  | SI | Waiting List Type |
| SMRE_WaitingTimeGuaranteeExc | varchar |  |  | SI | Waiting Time Guarantee Exception |
| SPRE_MainDiagnosis | varchar |  |  | SI | Main Diagnosis |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*