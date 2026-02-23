# SQLUser.LBC_ResultType

**Schema:** SQLUser
**Columnas:** 198
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCRT_RowID | bigint | PK |  | NO | - |
| ChildQ130DR | - |  |  | SI | Child Reference: Motivo de Consulta |
| LBCRT_Code | varchar |  |  | NO | Code |
| LBCRT_CreatedDate | date |  |  | SI | Created Date |
| LBCRT_CreatedTime | time |  |  | SI | Created Time |
| LBCRT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LBCRT_DateFrom | date |  |  | SI | Effective date for the record |
| LBCRT_DateTo | date |  |  | SI | Last day the record is active  |
| LBCRT_Desc | varchar |  |  | NO | Description |
| LBCRT_UpdatedDate | date |  |  | SI | Updated Date |
| LBCRT_UpdatedTime | time |  |  | SI | Updated Time |
| LBCRT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | CESFAM |
| Q02 | - |  |  | SI | Diabetes |
| Q03 | - |  |  | SI | Años Diagnóstico |
| Q04 | - |  |  | SI | Tratamiento |
| Q05 | - |  |  | SI | Último Fondo de Ojo |
| Q06 | - |  |  | SI | Hipertensión Arterial |
| Q10 | - |  |  | SI | Otras Enfermedades |
| Q100 | - |  |  | SI | Test de Schirmer |
| Q101 | - |  |  | SI | Estudio Estrabismo |
| Q102 | - |  |  | SI | Ciclopegía |
| Q103 | - |  |  | SI | Reflejo Fotomotor OD |
| Q103ObsDR | - |  |  | SI | Reflejo Fotomotor OD DR |
| Q104 | - |  |  | SI | Reflejo Fotomotor OI |
| Q104ObsDR | - |  |  | SI | Reflejo Fotomotor OI DR |
| Q105 | - |  |  | SI | Autorefractometría con cicloplegía OD de Esfera |
| Q106 | - |  |  | SI | Autorefractometría con cicloplegía OI de Esfera |
| Q107 | - |  |  | SI | Autorefractometría con cicloplegía DP |
| Q108 | - |  |  | SI | Autorefractometría con cicloplegía OD de Cilindro |
| Q109 | - |  |  | SI | Autorefractometría con cicloplegía OI de Cilindro |
| Q11 | - |  |  | SI | Antecedentes Glaucoma |
| Q110 | - |  |  | SI | Autorefractometría con cicloplegía OD grados |
| Q111 | - |  |  | SI | Autorefractometría con cicloplegía OI grados |
| Q112 | - |  |  | SI | Tratamiento 2 |
| Q113 | - |  |  | SI | Paquimetría central Observación |
| Q114 | - |  |  | SI | Fecha 1 |
| Q115 | - |  |  | SI | Fecha 2 |
| Q116 | - |  |  | SI | Fecha 3 |
| Q117 | - |  |  | SI | Fecha 4 |
| Q118 | - |  |  | SI | Fecha 5 |
| Q119 | - |  |  | SI | Fecha 6 |
| Q120 | - |  |  | SI | Fecha 7 |
| Q121 | - |  |  | SI | obs 1 |
| Q122 | - |  |  | SI | obs 2 |
| Q123 | - |  |  | SI | obs 3 |
| Q124 | - |  |  | SI | obs 4 |
| Q125 | - |  |  | SI | obs 5 |
| Q126 | - |  |  | SI | obs 6 |
| Q127 | - |  |  | SI | obs 7 |
| Q128 | - |  |  | SI | Ex via lagrimal OD |
| Q129 | - |  |  | SI | Ex via lagrimal OI |
| Q13 | - |  |  | SI | Lentes |
| Q131 | - |  |  | SI | Resultado General Visión Ojo Derecho |
| Q131ObsDR | - |  |  | SI | Resultado General Visión Ojo Derecho DR |
| Q132 | - |  |  | SI | Resultado General Visión Ojo Izquierdo |
| Q132ObsDR | - |  |  | SI | Resultado General Visión Ojo Izquierdo DR |
| Q133 | - |  |  | SI | Lentes |
| Q14 | - |  |  | SI | VOD SSL |
| Q14ObsDR | - |  |  | SI | VOD SSL DR |
| Q15 | - |  |  | SI | VOI SSL |
| Q15ObsDR | - |  |  | SI | VOI SSL DR |
| Q16 | - |  |  | SI | VOD CSL |
| Q16ObsDR | - |  |  | SI | VOD CSL DR |
| Q17 | - |  |  | SI | VOI CSL |
| Q17ObsDR | - |  |  | SI | VOI CSL DR |
| Q18 | - |  |  | SI | VOD CAE |
| Q18ObsDR | - |  |  | SI | VOD CAE DR |
| Q19 | - |  |  | SI | VOI CAE |
| Q19ObsDR | - |  |  | SI | VOI CAE DR |
| Q20 | - |  |  | SI | Tonometría Tn OD |
| Q20ObsDR | - |  |  | SI | Tonometría Tn OD DR |
| Q21 | - |  |  | SI | Tonometría Tn OI |
| Q21ObsDR | - |  |  | SI | Tonometría Tn OI DR |
| Q22 | - |  |  | SI | Rojo Pupilar OD |
| Q22ObsDR | - |  |  | SI | Rojo Pupilar OD DR |
| Q23 | - |  |  | SI | Lentes |
| Q24 | - |  |  | SI | Rojo Pupilar OI |
| Q24ObsDR | - |  |  | SI | Rojo Pupilar OI DR |
| Q25 | - |  |  | SI | Pupilas |
| Q25ObsDR | - |  |  | SI | Pupilas DR |
| Q26 | - |  |  | SI | Cámara Anterior OD |
| Q26ObsDR | - |  |  | SI | Cámara Anterior OD DR |
| Q27 | - |  |  | SI | Cámara Anterior OI |
| Q27ObsDR | - |  |  | SI | Cámara Anterior OI DR |
| Q28 | - |  |  | SI | Cover Test |
| Q29 | - |  |  | SI | Motilidad |
| Q30 | - |  |  | SI | T. Hishberg |
| Q31 | - |  |  | SI | PPC |
| Q32 | - |  |  | SI | Autorefractometría OD de Esfera |
| Q33 | - |  |  | SI | Autorefractometría OI de Esfera |
| Q34 | - |  |  | SI | Autorefractometría DP |
| Q35 | - |  |  | SI | Autorefractometría OD de Cilindro |
| Q36 | - |  |  | SI | Autorefractometría OI de Cilindro |
| Q37 | - |  |  | SI | Autorefractometría OD grados |
| Q38 | - |  |  | SI | Autorefractometría OI grados |
| Q39 | - |  |  | SI | Autorefractometría Observaciones |
| Q40 | - |  |  | SI | Lensometría OD de Esfera |
| Q41 | - |  |  | SI | Lensometría OI de Esfera |
| Q42 | - |  |  | SI | Lensometría DP |
| Q43 | - |  |  | SI | Lensometría OD de Cilindro |
| Q44 | - |  |  | SI | Lensometría OI de Cilindro |
| Q45 | - |  |  | SI | Lensometría OD grados |
| Q46 | - |  |  | SI | Lensometría OI grados |
| Q47 | - |  |  | SI | Lensometría Observaciones |
| Q48 | - |  |  | SI | BMC |
| Q49 | - |  |  | SI | Fondo de Ojo Izquierdo |
| Q49ObsDR | - |  |  | SI | Fondo de Ojo Izquierdo DR |
| Q50 | - |  |  | SI | Fondo de Ojo Derecho |
| Q50ObsDR | - |  |  | SI | Fondo de Ojo Derecho DR |
| Q51 | - |  |  | SI | Observaciones |
| Q52 | - |  |  | SI | Alta con |
| Q53 | - |  |  | SI | Control |
| Q54 | - |  |  | SI | Otro |
| Q55 | - |  |  | SI | Lente Lejos  OD de Esfera |
| Q56 | - |  |  | SI | Lente Lejos OI de Esfera |
| Q57 | - |  |  | SI | Lente Lejos DP |
| Q58 | - |  |  | SI | Lente Lejos  OD de Cilindro |
| Q59 | - |  |  | SI | Lente Lejos OI de Cilindro |
| Q60 | - |  |  | SI | Lente Lejos OD grados |
| Q61 | - |  |  | SI | Lente Lejos OI grados |
| Q62 | - |  |  | SI | Lente Lejos Observaciones |
| Q63 | - |  |  | SI | Lente Cerca OD de Esfera |
| Q64 | - |  |  | SI | Lente Cerca de Esfera |
| Q65 | - |  |  | SI | Lente Cerca DP |
| Q66 | - |  |  | SI | Lente Cerca OD de Cilindro |
| Q67 | - |  |  | SI | Lente Cerca OI de Cilindro |
| Q68 | - |  |  | SI | Lente Cerca  OD grados |
| Q69 | - |  |  | SI | Lente Cerca OI grados |
| Q70 | - |  |  | SI | Lente Cerca Observaciones |
| Q71 | - |  |  | SI | Lente Cerca ADD |
| Q72 | - |  |  | SI | Tratamiento |
| Q73 | - |  |  | SI | Dia 1 OD 8am |
| Q74 | - |  |  | SI | Dia 1 OD 12pm |
| Q75 | - |  |  | SI | Dia 1 OD 16pm |
| Q76 | - |  |  | SI | Dia 1 OI 8am |
| Q77 | - |  |  | SI | Dia 1 OI 12pm |
| Q78 | - |  |  | SI | Dia 1 OI 16pm |
| Q79 | - |  |  | SI | Dia 2 OD 8am |
| Q80 | - |  |  | SI | Dia 2 OD 12pm |
| Q81 | - |  |  | SI | Dia 2 OD 16pm |
| Q82 | - |  |  | SI | Dia 2 OI 8am |
| Q83 | - |  |  | SI | Dia 2 OI 12pm |
| Q84 | - |  |  | SI | Dia 2 OI 16pm |
| Q85 | - |  |  | SI | Cálculo Promedio OD |
| Q86 | - |  |  | SI | Cálculo Promedio OI |
| Q87 | - |  |  | SI | Paquimetría Central OD AVS |
| Q88 | - |  |  | SI | Paquimetría Central OI AVS |
| Q89 | - |  |  | SI | Paquimetría Central OD SD |
| Q90 | - |  |  | SI | Paquimetría Central OI SD |
| Q91 | - |  |  | SI | Paquimetría Central OD SD Obs |
| Q92 | - |  |  | SI | Paquimetría Central OI SD Obs |
| Q94 | - |  |  | SI | Paquimetría Central OD AVS Obs |
| Q95 | - |  |  | SI | Paquimetría Central OI AVS Obs |
| Q96 | - |  |  | SI | Curva Tensión |
| Q97 | - |  |  | SI | Campo Visual |
| Q98 | - |  |  | SI | Ortóptica |
| Q99 | - |  |  | SI | Examen Vía Lagrimal |
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