# questionnaire.QTCEPSTE6M

> Test de Provocación Bronquial con Ejercicio

**Schema:** questionnaire
**Columnas:** 153
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Test de Provocación Bronquial con Ejercicio

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| QCaidaFem | numeric |  |  | SI | % caida FEM |
| QCaidaFemAbs | numeric |  |  | SI | % Caida FEM Abs  |
| QCaidaFemCal | varchar |  |  | SI | % Caida FEM |
| QConclusion | varchar |  |  | SI | Conclusión |
| QCoope | varchar |  |  | SI | Cooperación |
| QEST | numeric |  |  | SI | Estatura |
| QEdad | varchar |  |  | SI | Edad |
| QEstBD10Min | varchar |  |  | SI | Estridor Post BD 10 Min |
| QEstBasalEJ | varchar |  |  | SI | Estridor Basal Prg.Ejercicio |
| QEstEJ2Min | varchar |  |  | SI | Estridor Prg Ejercicio 2 Min |
| QEstEJ6Min | varchar |  |  | SI | Estridor Prg Ejercicio 6 Min |
| QEstPostEJ10Min | varchar |  |  | SI | Estridor Post Ejercicio 10 Min |
| QEstPostEJ20Min | varchar |  |  | SI | Estridor Post Ejercicio 20 Min |
| QEstPostEJ3Min | varchar |  |  | SI | Estridor Post Ejercicio 3 Min |
| QEstPostEJ5Min | varchar |  |  | SI | Estridor Post Ejercicio 5 Min |
| QEtiquetaCaida | varchar |  |  | SI | POSITIVO  |
| QEtiquetaIndice | varchar |  |  | SI | POSITIVO |
| QFCBD10Min | varchar |  |  | SI | FC O2 Post BD 10 Min |
| QFCBD10MinObsDR | varchar |  | FK | SI | FC O2 Post BD 10 Min DR |
| QFCBasalEJ | varchar |  |  | SI | FC Basal Prg.Ejercicio |
| QFCBasalEJObsDR | varchar |  | FK | SI | FC Basal Prg.Ejercicio DR |
| QFCEJ2Min | varchar |  |  | SI | FC O2 Prg Ejercicio 2 Min |
| QFCEJ2MinObsDR | varchar |  | FK | SI | FC O2 Prg Ejercicio 2 Min DR |
| QFCEJ6Min | varchar |  |  | SI | FC O2 Prg Ejercicio 6 Min |
| QFCEJ6MinObsDR | varchar |  | FK | SI | FC O2 Prg Ejercicio 6 Min DR |
| QFCMAX | varchar |  |  | SI | FC Max.Teórica |
| QFCPostEJ10Min | varchar |  |  | SI | FC O2 Post Ejercicio 10 Min |
| QFCPostEJ10MinObsDR | varchar |  | FK | SI | FC O2 Post Ejercicio 10 Min DR |
| QFCPostEJ20Min | varchar |  |  | SI | FC O2 Post Ejercicio 20 Min |
| QFCPostEJ20MinObsDR | varchar |  | FK | SI | FC O2 Post Ejercicio 20 Min DR |
| QFCPostEJ3Min | varchar |  |  | SI | FC O2 Post Ejercicio 3 Min |
| QFCPostEJ3MinObsDR | varchar |  | FK | SI | FC O2 Post Ejercicio 3 Min DR |
| QFCPostEJ5Min | varchar |  |  | SI | FC O2 Post Ejercicio 5 Min |
| QFCPostEJ5MinObsDR | varchar |  | FK | SI | FC O2 Post Ejercicio 5 Min DR |
| QFECHATEST | date |  |  | SI | Fecha Test |
| QFEMBAS | numeric |  |  | SI | FEM Basal |
| QFEMTEO | numeric |  |  | SI | FEM Teórico |
| QFemBD10Min | numeric |  |  | SI | FEM Post BD 10 Min |
| QFemBasalEJ | numeric |  |  | SI | FEM Basal Prg.Ejercicio |
| QFemEJ2Min | numeric |  |  | SI | FEM Prg Ejercicio 2 Min |
| QFemEJ6Min | numeric |  |  | SI | FEM Prg Ejercicio 6 Min |
| QFemPostEJ10Min | numeric |  |  | SI | FEM Post Ejercicio 10 Min |
| QFemPostEJ20Min | numeric |  |  | SI | FEM Post Ejercicio 20 Min |
| QFemPostEJ3Min | numeric |  |  | SI | FEM Post Ejercicio 3 Min |
| QFemPostEJ5Min | numeric |  |  | SI | FEM Post Ejercicio 5 Min |
| QHR | numeric |  |  | SI | H.R. |
| QIndiceAlza | numeric |  |  | SI | Indice Alza % |
| QIndiceLab | numeric |  |  | SI | Indice Labilidad |
| QIndiceLabCal | varchar |  |  | SI | Indice labilidad Cal |
| QMPBD10Min | varchar |  |  | SI | MP Post BD 10 Min |
| QMPBasalEJ | varchar |  |  | SI | MP Basal Prg.Ejercicio |
| QMPEJ2Min | varchar |  |  | SI | MP Prg Ejercicio 2 Min |
| QMPEJ6Min | varchar |  |  | SI | MP Prg Ejercicio 6 Min |
| QMPPostEJ10Min | varchar |  |  | SI | MP Post Ejercicio 10 Min |
| QMPPostEJ20Min | varchar |  |  | SI | MP Post Ejercicio 20 Min |
| QMPPostEJ3Min | varchar |  |  | SI | MP Post Ejercicio 3 Min |
| QMPPostEJ5Min | varchar |  |  | SI | MP Post Ejercicio 5 Min |
| QNFicha | varchar |  |  | SI | N° Ficha |
| QObs | varchar |  |  | SI | Observaciones |
| QOtro | varchar |  |  | SI | Otro Desc |
| QOtroBD10Min | varchar |  |  | SI | Otro Post BD 10 Min |
| QOtroBasalEJ | varchar |  |  | SI | Otro Basal Prg.Ejercicio |
| QOtroEJ2Min | varchar |  |  | SI | Otro Prg Ejercicio 2 Min |
| QOtroEJ6Min | varchar |  |  | SI | Otro Prg Ejercicio 6 Min |
| QOtroPostEJ10Min | varchar |  |  | SI | Otro Post Ejercicio 10 Min |
| QOtroPostEJ20Min | varchar |  |  | SI | Otro Post Ejercicio 20 Min |
| QOtroPostEJ3Min | varchar |  |  | SI | Otro Post Ejercicio 3 Min |
| QOtroPostEJ5Min | varchar |  |  | SI | Otro Post Ejercicio 5 Min |
| QPeso | numeric |  |  | SI | Peso |
| QRedFemBD10Min | varchar |  |  | SI | Reduc.FEM Post BD 10 Min |
| QRedFemBasalEJ | varchar |  |  | SI | Reduc.FEM Basal Prg.Ejercicio |
| QRedFemEJ2Min | varchar |  |  | SI | Reduc.FEM Prg Ejercicio 2 Min |
| QRedFemEJ6Min | varchar |  |  | SI | Reduc.FEM Prg Ejercicio 6 Min |
| QRedFemPostEJ10Min | varchar |  |  | SI | Reduc.FEM Post Ejercicio 10 Min |
| QRedFemPostEJ20Min | varchar |  |  | SI | Reduc.FEM Post Ejercicio 20 Min |
| QRedFemPostEJ3Min | varchar |  |  | SI | Reduc.FEM Post Ejercicio 3 Min |
| QRedFemPostEJ5Min | varchar |  |  | SI | Reduc.FEM Post Ejercicio 5 Min |
| QRonBD10Min | varchar |  |  | SI | Roncus Post BD 10 Min |
| QRonBasalEJ | varchar |  |  | SI | Roncus Basal Prg.Ejercicio |
| QRonEJ2Min | varchar |  |  | SI | Roncus Prg Ejercicio 2 Min |
| QRonEJ6Min | varchar |  |  | SI | Roncus Prg Ejercicio 6 Min |
| QRonPostEJ10Min | varchar |  |  | SI | Roncus Post Ejercicio 10 Min |
| QRonPostEJ20Min | varchar |  |  | SI | Roncus Post Ejercicio 20 Min |
| QRonPostEJ3Min | varchar |  |  | SI | Roncus Post Ejercicio 3 Min |
| QRonPostEJ5Min | varchar |  |  | SI | Roncus Post Ejercicio 5 Min |
| QSIBBD10Min | varchar |  |  | SI | Sibilancias Post BD 10 Min |
| QSIBBasalEJ | varchar |  |  | SI | Sibilancias Basal Prg.Ejercicio |
| QSIBEJ2Min | varchar |  |  | SI | Sibilancias Prg Ejercicio 2 Min |
| QSIBEJ6Min | varchar |  |  | SI | Sibilancias Prg Ejercicio 6 Min |
| QSIBPostEJ10Min | varchar |  |  | SI | Sibilancias Post Ejercicio 10 Min |
| QSIBPostEJ20Min | varchar |  |  | SI | Sibilancias Post Ejercicio 20 Min |
| QSIBPostEJ3Min | varchar |  |  | SI | Sibilancias Post Ejercicio 3 Min |
| QSIBPostEJ5Min | varchar |  |  | SI | Sibilancias Post Ejercicio 5 Min |
| QSatBD10Min | numeric |  |  | SI | Sat O2 Post BD 10 Min |
| QSatBasalEJ | numeric |  |  | SI | Sat Basal Prg.Ejercicio |
| QSatEJ2Min | numeric |  |  | SI | Sat O2 Prg Ejercicio 2 Min |
| QSatEJ6Min | numeric |  |  | SI | Sat O2 Prg Ejercicio 6 Min |
| QSatPostEJ10Min | numeric |  |  | SI | Sat O2 Post Ejercicio 10 Min |
| QSatPostEJ20Min | numeric |  |  | SI | Sat O2 Post Ejercicio 20 Min |
| QSatPostEJ3Min | numeric |  |  | SI | Sat O2 Post Ejercicio 3 Min |
| QSatPostEJ5Min | numeric |  |  | SI | Sat O2 Post Ejercicio 5 Min |
| QSexo | varchar |  |  | SI | Sexo |
| QTEMP | numeric |  |  | SI | Temperatura |
| QTosBD10Min | varchar |  |  | SI | Tos Post BD 10 Min |
| QTosBasalEJ | varchar |  |  | SI | Tos Basal Prg.Ejercicio |
| QTosEJ2Min | varchar |  |  | SI | Tos Prg Ejercicio 2 Min |
| QTosEJ6Min | varchar |  |  | SI | Tos Prg Ejercicio 6 Min |
| QTosPostEJ10Min | varchar |  |  | SI | Tos Post Ejercicio 10 Min |
| QTosPostEJ20Min | varchar |  |  | SI | Tos Post Ejercicio 20 Min |
| QTosPostEJ3Min | varchar |  |  | SI | Tos Post Ejercicio 3 Min |
| QTosPostEJ5Min | varchar |  |  | SI | Tos Post Ejercicio 5 Min |
| QUESAnaDR | varchar |  | FK | SI | Anaesthesia |
| QUESAnaOperationDR | varchar |  | FK | SI | Operation |
| QUESConsultDR | varchar |  | FK | SI | Consult |
| QUESCopiedComments | varchar |  |  | SI | Copied Comments |
| QUESCopiedDate | date |  |  | SI | Copied Date |
| QUESCopiedEpDR | bigint |  | FK | SI | Copied Episode |
| QUESCopiedSourceDR | bigint |  | FK | SI | Copied Source DR |
| QUESCopiedTime | time |  |  | SI | Copied Time |
| QUESCopiedUserDR | bigint |  | FK | SI | Copied User |
| QUESCreateDate | date |  |  | SI | Creation Date |
| QUESCreateTime | time |  |  | SI | Creation Time |
| QUESCreateUserDR | bigint |  | FK | SI | Creation User |
| QUESDate | date |  |  | SI | Last Update Date |
| QUESErrorReasonDR | bigint |  | FK | SI | Error Reason |
| QUESFHResidentDR | bigint |  | FK | SI | Resident |
| QUESMRClinicalPathWaysDR | varchar |  | FK | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | varchar |  | FK | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | varchar |  | FK | SI | Order Execution |
| QUESORPreanaestheticConsultDR | bigint |  | FK | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | varchar |  | FK | SI | Observation Entry |
| QUESOperRoomDR | bigint |  | FK | SI | Operating Room |
| QUESPAAdmDR | bigint |  | FK | SI | Admission |
| QUESPAAdverseEventDR | varchar |  | FK | SI | Adverse Event |
| QUESPAPatMasDR | bigint |  | FK | SI | Patient |
| QUESPAPregnancyDR | bigint |  | FK | SI | Pregnancy |
| QUESPAWaitingListDR | bigint |  | FK | SI | Waiting List |
| QUESPathwayItemDR | varchar |  | FK | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | varchar |  | FK | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | varchar |  | FK | SI | Appointments |
| QUESRBApptOutcomeDR | varchar |  | FK | SI | Appointment Outcome |
| QUESRBApptSlotDR | varchar |  | FK | SI | Appointment Slot |
| QUESReasonForCorrectionDR | bigint |  | FK | SI | Reason for Correction |
| QUESSSUserDefWindowDR | bigint |  | FK | SI | Questionnaire |
| QUESScore | varchar |  |  | SI | Score |
| QUESSecondUserDR | bigint |  | FK | SI | Second Signature |
| QUESStatusDR | bigint |  | FK | SI | Status |
| QUESTextResultDR | bigint |  | FK | SI | Text Result |
| QUESTime | time |  |  | SI | Last Update Time |
| QUESTransactionDR | varchar |  | FK | SI | Transaction |
| QUESUserDR | bigint |  | FK | SI | Last Update User |
| QUsoCor | varchar |  |  | SI | Uso Corticoides Inhalados |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*