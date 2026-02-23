# SQLUser.LBC_AppEventRule

**Schema:** SQLUser
**Columnas:** 146
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCAER_RowID | bigint | PK |  | NO | - |
| LBCAER_AdmType | varchar |  |  | SI | Patient / Episode
-------------
Admission Type |
| LBCAER_AgeFrom | double |  |  | SI | Age Range From (format [yy].mmdd , ddd is 0-1231)... |
| LBCAER_AgeTo | double |  |  | SI | Age Range To (format [yy].mmdd , mmdd is 0-1231)
... |
| LBCAER_AnatomicalSiteQualifiers | varchar |  |  | SI | Anatomical Site Qualifier |
| LBCAER_AnatomicalSites | varchar |  |  | SI | Anatomical Site |
| LBCAER_CareProvGroups | varchar |  |  | SI | Care Provider Groups |
| LBCAER_CareProvSpecialities | varchar |  |  | SI | Care Provider Specialities |
| LBCAER_CareProvs | varchar |  |  | SI | Care Provider |
| LBCAER_ClinicalConditions | varchar |  |  | SI | Clinical Conditions |
| LBCAER_ClinicalInterpretations | varchar |  |  | SI | Actions
------------
Clinical Interpretations |
| LBCAER_CodeTableTags | varchar |  |  | SI | Code Table
--------
List of code table Tags |
| LBCAER_CreatedDate | date |  |  | SI | Created Date |
| LBCAER_CreatedTime | time |  |  | SI | Created Time |
| LBCAER_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LBCAER_DateFrom | date |  |  | SI | Effective date for the record |
| LBCAER_DateTo | date |  |  | SI | Last day the record is active  |
| LBCAER_Description | varchar |  |  | NO | General Properties
--------------
Description |
| LBCAER_Group | numeric |  |  | SI | Group |
| LBCAER_InstrumentGroups | varchar |  |  | SI | Instrument Groups |
| LBCAER_Instruments | varchar |  |  | SI | Instruments |
| LBCAER_Lesions | varchar |  |  | SI | Lesion |
| LBCAER_Owner | varchar |  |  | SI | Owner |
| LBCAER_PatType_DR | bigint |  | FK | SI | Patient Type |
| LBCAER_PatientFlags | varchar |  |  | SI | Patient Flags |
| LBCAER_PatientLocations | varchar |  |  | SI | Patient Locations |
| LBCAER_PerformedAtLabSite_DR | bigint |  | FK | SI | Performed at Lab Site |
| LBCAER_Pregnant | varchar |  |  | SI | Pregnant. |
| LBCAER_ReferringDoctors | varchar |  |  | SI | Referring Doctors |
| LBCAER_Sequence | numeric |  |  | NO | Sequence within the group |
| LBCAER_Sex_DR | bigint |  | FK | SI | Sex
Compared with LBEPSexDR |
| LBCAER_Species | varchar |  |  | SI | Species |
| LBCAER_SpeciesBreeds | varchar |  |  | SI | Breeds |
| LBCAER_SpecimenGroup_DR | bigint |  | FK | SI | Specimen
-------------
Specimen Group |
| LBCAER_Specimens | varchar |  |  | SI | Specimen |
| LBCAER_SubjectType_DR | bigint |  | FK | SI | SubjectType |
| LBCAER_TSClinicalReview | varchar |  |  | SI | Clinical Review |
| LBCAER_TSConfidential | varchar |  |  | SI | Test Set Confidental. |
| LBCAER_TSExpiredSpcValidity | varchar |  |  | SI | Test Set Expired Specimen Validity
Compared with ... |
| LBCAER_TSIExpiredSpcValidity | varchar |  |  | SI | Test Set Item
--------------
Test Set Item Expri... |
| LBCAER_TSLabSite_DR | bigint |  | FK | SI | Test Set Lab Site |
| LBCAER_TSPriorities | varchar |  |  | SI | Test Set
-----------
Test Priority |
| LBCAER_TSSignificantResult | varchar |  |  | SI | Significant Result. |
| LBCAER_TestMethods | varchar |  |  | SI | Test Methods |
| LBCAER_TestSetItem_DR | varchar |  | FK | SI | Test Set Revision Item Reference |
| LBCAER_TestSet_DR | bigint |  | FK | SI | Test Set Revision Reference |
| LBCAER_Type | varchar |  |  | NO | Type |
| LBCAER_UpdatedDate | date |  |  | SI | Updated Date |
| LBCAER_UpdatedTime | time |  |  | SI | Updated Time |
| LBCAER_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Edad Menarquia (años) |
| Q02 | - |  |  | SI | Edad de Menopausia (años) |
| Q03 | - |  |  | SI | Tiempo de Menopausia (años) |
| Q04 | - |  |  | SI | Tiempo de Menopausia (meses) |
| Q05 | - |  |  | SI | Tiempo de Menopausia (dias) |
| Q06 | - |  |  | SI | Tipo de Menopausia |
| Q06A | - |  |  | SI | Menopausia Quirúrgica |
| Q07 | - |  |  | SI | Menopausia Quirúrgica |
| Q08 | - |  |  | SI | N° de Gestas |
| Q09 | - |  |  | SI | N° Partos |
| Q10 | - |  |  | SI | N° Abortos |
| Q11 | - |  |  | SI | Consumo Cigarrillos |
| Q12 | - |  |  | SI | N° Cigarrillos (Paquetes por Año) |
| Q13 | - |  |  | SI | Actividad Física |
| Q14 | - |  |  | SI | Actividad Sexual |
| Q15 | - |  |  | SI | Antecedentes de Fracturas |
| Q16 | - |  |  | SI | Falla Ovárica Prematura |
| Q17 | - |  |  | SI | Peso (Kg) |
| Q17ObsDR | - |  |  | SI | Peso (Kg) DR |
| Q18 | - |  |  | SI | Talla (Cms) |
| Q18ObsDR | - |  |  | SI | Talla (Cms) DR |
| Q19 | - |  |  | SI | Indice Masa Corporal |
| Q19ObsDR | - |  |  | SI | Indice Masa Corporal DR |
| Q20 | - |  |  | SI | Circunferencia Cintura |
| Q20ObsDR | - |  |  | SI | Circunferencia Cintura DR |
| Q21 | - |  |  | SI | Estado Nutricional |
| Q21ObsDR | - |  |  | SI | Estado Nutricional DR |
| Q22 | - |  |  | SI | Presión Arterial Sistólica |
| Q22ObsDR | - |  |  | SI | Presión Arterial Sistólica DR |
| Q23 | - |  |  | SI | Presión Arterial Diastólica |
| Q23ObsDR | - |  |  | SI | Presión Arterial Diastólica DR |
| Q24 | - |  |  | SI | Resultado examen físico de Mamas |
| Q24ObsDR | - |  |  | SI | Resultado examen físico de Mamas DR |
| Q25 | - |  |  | SI | Varices |
| Q26 | - |  |  | SI | Genitales externo |
| Q27 | - |  |  | SI | Vulva |
| Q28 | - |  |  | SI | Vagina |
| Q29 | - |  |  | SI | Cuello uterino |
| Q30 | - |  |  | SI | Cuerpo uterino |
| Q31 | - |  |  | SI | Anexos |
| Q49 | - |  |  | SI | Trombosis activa o estados protombóticos |
| Q50 | - |  |  | SI | Enfermedad coronaria |
| Q51 | - |  |  | SI | Accidente Vascular |
| Q52 | - |  |  | SI | Cáncer de Mama |
| Q53 | - |  |  | SI | Hiperplasia endometrial |
| Q54 | - |  |  | SI | Adenocarcinoma de endometrio |
| Q55 | - |  |  | SI | Adenocarcinoma de cuello uterino |
| Q56 | - |  |  | SI | Sangrado uterino de etiología no precisada |
| Q57 | - |  |  | SI | Insuficiencia hepática aguda |
| Q58 | - |  |  | SI | Indicación terapia hormonal |
| Q59 | - |  |  | SI | Fecha inicio terapia hormonal |
| Q60 | - |  |  | SI | Metodo prescrito |
| Q61 | - |  |  | SI | Otro Método prescrito |
| Q89 | - |  |  | SI | Tipo de Menopausia novo |
| Q90 | - |  |  | SI | Menopausia Quirúrgica |
| QIMC | - |  |  | SI | IMC |
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