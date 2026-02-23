# questionnaire.QTCEFUAPO

> Ficha Unidad de Atención Primaria Oftalmológica (UAPO)

**Schema:** questionnaire
**Columnas:** 187
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Ficha Unidad de Atención Primaria Oftalmológica (UAPO)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | CESFAM |
| Q02 | varchar |  |  | SI | Diabetes |
| Q03 | numeric |  |  | SI | Años Diagnóstico |
| Q04 | varchar |  |  | SI | Tratamiento |
| Q05 | date |  |  | SI | Último Fondo de Ojo |
| Q06 | varchar |  |  | SI | Hipertensión Arterial |
| Q10 | varchar |  |  | SI | Otras Enfermedades |
| Q100 | varchar |  |  | SI | Test de Schirmer |
| Q101 | varchar |  |  | SI | Estudio Estrabismo |
| Q102 | varchar |  |  | SI | Ciclopegía |
| Q103 | varchar |  |  | SI | Reflejo Fotomotor OD |
| Q103ObsDR | varchar |  | FK | SI | Reflejo Fotomotor OD DR |
| Q104 | varchar |  |  | SI | Reflejo Fotomotor OI |
| Q104ObsDR | varchar |  | FK | SI | Reflejo Fotomotor OI DR |
| Q105 | varchar |  |  | SI | Autorefractometría con cicloplegía OD de Esfera |
| Q106 | varchar |  |  | SI | Autorefractometría con cicloplegía OI de Esfera |
| Q107 | numeric |  |  | SI | Autorefractometría con cicloplegía DP |
| Q108 | varchar |  |  | SI | Autorefractometría con cicloplegía OD de Cilindro |
| Q109 | varchar |  |  | SI | Autorefractometría con cicloplegía OI de Cilindro |
| Q11 | varchar |  |  | SI | Antecedentes Glaucoma |
| Q110 | varchar |  |  | SI | Autorefractometría con cicloplegía OD grados |
| Q111 | varchar |  |  | SI | Autorefractometría con cicloplegía OI grados |
| Q112 | varchar |  |  | SI | Tratamiento 2 |
| Q113 | varchar |  |  | SI | Paquimetría central Observación |
| Q114 | date |  |  | SI | Fecha 1 |
| Q115 | date |  |  | SI | Fecha 2 |
| Q116 | date |  |  | SI | Fecha 3 |
| Q117 | date |  |  | SI | Fecha 4 |
| Q118 | date |  |  | SI | Fecha 5 |
| Q119 | date |  |  | SI | Fecha 6 |
| Q120 | date |  |  | SI | Fecha 7 |
| Q121 | varchar |  |  | SI | obs 1 |
| Q122 | varchar |  |  | SI | obs 2 |
| Q123 | varchar |  |  | SI | obs 3 |
| Q124 | varchar |  |  | SI | obs 4 |
| Q125 | varchar |  |  | SI | obs 5 |
| Q126 | varchar |  |  | SI | obs 6 |
| Q127 | varchar |  |  | SI | obs 7  |
| Q128 | varchar |  |  | SI | Ex via lagrimal OD |
| Q129 | varchar |  |  | SI | Ex via lagrimal OI |
| Q13 | varchar |  |  | SI | Lentes |
| Q131 | varchar |  |  | SI | Resultado General Visión Ojo Derecho |
| Q131ObsDR | varchar |  | FK | SI | Resultado General Visión Ojo Derecho DR |
| Q132 | varchar |  |  | SI | Resultado General Visión Ojo Izquierdo |
| Q132ObsDR | varchar |  | FK | SI | Resultado General Visión Ojo Izquierdo DR |
| Q133 | varchar |  |  | SI | Lentes |
| Q14 | varchar |  |  | SI | VOD SSL |
| Q14ObsDR | varchar |  | FK | SI | VOD SSL DR |
| Q15 | varchar |  |  | SI | VOI SSL |
| Q15ObsDR | varchar |  | FK | SI | VOI SSL DR |
| Q16 | varchar |  |  | SI | VOD CSL |
| Q16ObsDR | varchar |  | FK | SI | VOD CSL DR |
| Q17 | varchar |  |  | SI | VOI CSL |
| Q17ObsDR | varchar |  | FK | SI | VOI CSL DR |
| Q18 | varchar |  |  | SI | VOD CAE |
| Q18ObsDR | varchar |  | FK | SI | VOD CAE DR |
| Q19 | varchar |  |  | SI | VOI CAE |
| Q19ObsDR | varchar |  | FK | SI | VOI CAE DR |
| Q20 | varchar |  |  | SI | Tonometría Tn OD |
| Q20ObsDR | varchar |  | FK | SI | Tonometría Tn OD DR |
| Q21 | varchar |  |  | SI | Tonometría Tn OI |
| Q21ObsDR | varchar |  | FK | SI | Tonometría Tn OI DR |
| Q22 | varchar |  |  | SI | Rojo Pupilar OD |
| Q22ObsDR | varchar |  | FK | SI | Rojo Pupilar OD DR |
| Q23 | varchar |  |  | SI | Lentes |
| Q24 | varchar |  |  | SI | Rojo Pupilar OI |
| Q24ObsDR | varchar |  | FK | SI | Rojo Pupilar OI DR |
| Q25 | varchar |  |  | SI | Pupilas |
| Q25ObsDR | varchar |  | FK | SI | Pupilas DR |
| Q26 | varchar |  |  | SI | Cámara Anterior OD |
| Q26ObsDR | varchar |  | FK | SI | Cámara Anterior OD DR |
| Q27 | varchar |  |  | SI | Cámara Anterior OI |
| Q27ObsDR | varchar |  | FK | SI | Cámara Anterior OI DR |
| Q28 | varchar |  |  | SI | Cover Test |
| Q29 | varchar |  |  | SI | Motilidad |
| Q30 | varchar |  |  | SI | T. Hishberg |
| Q31 | varchar |  |  | SI | PPC |
| Q32 | varchar |  |  | SI | Autorefractometría OD de Esfera |
| Q33 | varchar |  |  | SI | Autorefractometría OI de Esfera |
| Q34 | numeric |  |  | SI | Autorefractometría DP |
| Q35 | varchar |  |  | SI | Autorefractometría OD de Cilindro |
| Q36 | varchar |  |  | SI | Autorefractometría OI de Cilindro |
| Q37 | varchar |  |  | SI | Autorefractometría OD grados |
| Q38 | varchar |  |  | SI | Autorefractometría OI grados |
| Q39 | varchar |  |  | SI | Autorefractometría Observaciones |
| Q40 | varchar |  |  | SI | Lensometría OD de Esfera |
| Q41 | varchar |  |  | SI | Lensometría OI de Esfera |
| Q42 | numeric |  |  | SI | Lensometría DP |
| Q43 | varchar |  |  | SI | Lensometría OD de Cilindro |
| Q44 | varchar |  |  | SI | Lensometría OI de Cilindro |
| Q45 | varchar |  |  | SI | Lensometría OD grados |
| Q46 | varchar |  |  | SI | Lensometría OI grados |
| Q47 | varchar |  |  | SI | Lensometría Observaciones |
| Q48 | varchar |  |  | SI | BMC |
| Q49 | varchar |  |  | SI | Fondo de Ojo Izquierdo |
| Q49ObsDR | varchar |  | FK | SI | Fondo de Ojo Izquierdo DR |
| Q50 | varchar |  |  | SI | Fondo de Ojo Derecho |
| Q50ObsDR | varchar |  | FK | SI | Fondo de Ojo Derecho DR |
| Q51 | varchar |  |  | SI | Observaciones |
| Q52 | varchar |  |  | SI | Alta con |
| Q53 | varchar |  |  | SI | Control |
| Q54 | varchar |  |  | SI | Otro |
| Q55 | varchar |  |  | SI | Lente Lejos  OD de Esfera |
| Q56 | varchar |  |  | SI | Lente Lejos OI de Esfera |
| Q57 | numeric |  |  | SI | Lente Lejos DP |
| Q58 | varchar |  |  | SI | Lente Lejos  OD de Cilindro |
| Q59 | varchar |  |  | SI | Lente Lejos OI de Cilindro |
| Q60 | varchar |  |  | SI | Lente Lejos OD grados |
| Q61 | varchar |  |  | SI | Lente Lejos OI grados |
| Q62 | varchar |  |  | SI | Lente Lejos Observaciones |
| Q63 | varchar |  |  | SI | Lente Cerca OD de Esfera |
| Q64 | varchar |  |  | SI | Lente Cerca de Esfera |
| Q65 | numeric |  |  | SI | Lente Cerca DP |
| Q66 | varchar |  |  | SI | Lente Cerca OD de Cilindro |
| Q67 | varchar |  |  | SI | Lente Cerca OI de Cilindro |
| Q68 | varchar |  |  | SI | Lente Cerca  OD grados |
| Q69 | varchar |  |  | SI | Lente Cerca OI grados |
| Q70 | varchar |  |  | SI | Lente Cerca Observaciones |
| Q71 | varchar |  |  | SI | Lente Cerca ADD |
| Q72 | varchar |  |  | SI | Tratamiento |
| Q73 | varchar |  |  | SI | Dia 1 OD 8am |
| Q74 | varchar |  |  | SI | Dia 1 OD 12pm |
| Q75 | varchar |  |  | SI | Dia 1 OD 16pm |
| Q76 | varchar |  |  | SI | Dia 1 OI 8am |
| Q77 | varchar |  |  | SI | Dia 1 OI 12pm |
| Q78 | varchar |  |  | SI | Dia 1 OI 16pm |
| Q79 | varchar |  |  | SI | Dia 2 OD 8am |
| Q80 | varchar |  |  | SI | Dia 2 OD 12pm |
| Q81 | varchar |  |  | SI | Dia 2 OD 16pm |
| Q82 | varchar |  |  | SI | Dia 2 OI 8am |
| Q83 | varchar |  |  | SI | Dia 2 OI 12pm |
| Q84 | varchar |  |  | SI | Dia 2 OI 16pm |
| Q85 | varchar |  |  | SI | Cálculo Promedio OD |
| Q86 | varchar |  |  | SI | Cálculo Promedio OI |
| Q87 | varchar |  |  | SI | Paquimetría Central OD AVS |
| Q88 | varchar |  |  | SI | Paquimetría Central OI AVS |
| Q89 | varchar |  |  | SI | Paquimetría Central OD SD |
| Q90 | varchar |  |  | SI | Paquimetría Central OI SD |
| Q91 | varchar |  |  | SI | Paquimetría Central OD SD Obs |
| Q92 | varchar |  |  | SI | Paquimetría Central OI SD Obs |
| Q94 | varchar |  |  | SI | Paquimetría Central OD AVS Obs |
| Q95 | varchar |  |  | SI | Paquimetría Central OI AVS Obs |
| Q96 | varchar |  |  | SI | Curva Tensión |
| Q97 | varchar |  |  | SI | Campo Visual |
| Q98 | varchar |  |  | SI | Ortóptica |
| Q99 | varchar |  |  | SI | Examen Vía Lagrimal |
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

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*