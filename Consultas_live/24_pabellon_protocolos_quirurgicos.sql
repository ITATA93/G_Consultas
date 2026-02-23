-- ============================================================================
-- QUERY: PABELLON - PROTOCOLOS QUIRURGICOS COMPLETOS
-- Fecha: 2026-02-19
-- Descripción: Consulta integral de pabellón que incluye:
--   1. Programación quirúrgica (RB_OperatingRoom) con estados de booking
--   2. Registro de anestesia (OR_Anaesthesia) con estados y timeline
--   3. Detalle de operación (OR_Anaest_Operation) con estados de protocolo
--   4. Información completa de pacientes (PA_PatMas + PA_Adm)
--   5. Catálogos de referencia (ORC_Operation, CT_CareProv, PAC_StatePPP)
--
-- TABLAS INVOLUCRADAS:
--   RB_OperatingRoom     -> Programación/Booking de pabellón
--   OR_Anaesthesia       -> Registro anestésico (hijo de PA_Adm)
--   OR_Anaest_Operation  -> Detalle quirúrgico (hijo de OR_Anaesthesia)
--   PA_Adm               -> Episodio de atención
--   PA_PatMas             -> Datos maestros del paciente
--   PA_Person             -> Datos demográficos extendidos
--   ORC_Operation         -> Catálogo de operaciones (ICD)
--   CT_CareProv           -> Profesionales de salud
--   PAC_StatePPP          -> Catálogo de estados de protocolo
--
-- ESTADOS DEL BOOKING (RBOP_Status):
--   P = Programado, A = Admitido/Llegado, I = En curso,
--   C = Completado, X = Cancelado, S = Suspendido
--
-- SEGURIDAD: Solo SELECT con TOP. Sin modificación de datos.
-- ============================================================================

-- ============================================================================
-- QUERY 1: VISTA COMPLETA DE PABELLON (Booking + Paciente + Cirujano)
-- Uso: Tabla quirúrgica del día con todos los estados
-- ============================================================================
SELECT TOP 200
    -- === IDENTIFICACIÓN PROGRAMACIÓN ===
    RBOP.RBOP_RowId                     AS ID_Booking,
    RBOP.RBOP_BookingNumber             AS Num_Reserva,
    RBOP.RBOP_SequenceNo                AS Secuencia,

    -- === ESTADO DEL BOOKING ===
    RBOP.RBOP_Status                    AS Estado_Booking,
    CASE RBOP.RBOP_Status
        WHEN 'P' THEN 'Programado'
        WHEN 'A' THEN 'Admitido/Llegado'
        WHEN 'I' THEN 'En Curso'
        WHEN 'C' THEN 'Completado'
        WHEN 'X' THEN 'Cancelado'
        WHEN 'S' THEN 'Suspendido'
        ELSE RBOP.RBOP_Status
    END                                 AS Estado_Booking_Desc,
    RBOP.RBOP_Arrived                   AS Paciente_Llego,
    RBOP.RBOP_SetupComplete             AS Setup_Completo,
    RBOP.RBOP_CancelReason              AS Razon_Cancelacion,
    RBOP.RBOP_BookingType               AS Tipo_Reserva,
    RBOP.RBOP_DaySurgery                AS Cirugia_Ambulatoria,

    -- === DATOS DEL PACIENTE ===
    Pat.PAPMI_RowId                     AS ID_Paciente,
    Pat.PAPMI_No                        AS Num_Ficha,
    Pat.PAPMI_ID                        AS RUT_Paciente,
    Pat.PAPMI_Name                      AS Apellido_Paterno,
    Pat.PAPMI_Name2                     AS Nombre_Paciente,
    Pat.PAPMI_DOB                       AS Fecha_Nacimiento,

    -- === EPISODIO ===
    Adm.PAADM_RowId                     AS ID_Episodio,
    Adm.PAADM_ADMNo                     AS Num_Admision,
    Adm.PAADM_Type                      AS Tipo_Episodio,
    Adm.PAADM_AdmDate                   AS Fecha_Admision,

    -- === FECHAS DE PROGRAMACIÓN ===
    RBOP.RBOP_DateOper                  AS Fecha_Cirugia,
    RBOP.RBOP_TimeOper                  AS Hora_Cirugia,
    RBOP.RBOP_RequestedDateOper         AS Fecha_Solicitada,
    RBOP.RBOP_DateBook                  AS Fecha_Reserva,

    -- === PROCEDIMIENTO ===
    RBOP.RBOP_Procedure                 AS Procedimiento_Texto,
    RBOP.RBOP_ProcsOpers                AS Procedimientos_Operaciones,
    RBOP.RBOP_PreOpDiagnosis            AS Diagnostico_PreOp,
    RBOP.RBOP_AdmDiagnosis              AS Diagnostico_Admision,

    -- === EQUIPO QUIRÚRGICO (desde booking) ===
    RBOP.RBOP_Surgeon_DR                AS ID_Cirujano,
    RBOP.RBOP_SurgeonAssist_DR          AS ID_Cirujano_Asistente,
    RBOP.RBOP_Anaesthetist_DR           AS ID_Anestesiologo,
    RBOP.RBOP_OTConsultant_DR           AS ID_Consultor_OT,

    -- === TIEMPOS PLANIFICADOS ===
    RBOP.RBOP_EstimatedTime             AS Tiempo_Estimado,
    RBOP.RBOP_PlanSurgicalTime          AS Tiempo_Qx_Planificado_Min,
    RBOP.RBOP_PlanAnaesTime             AS Tiempo_Anest_Planificado_Min,
    RBOP.RBOP_PlanCleanUpTime           AS Tiempo_Limpieza_Min,
    RBOP.RBOP_TotalPlanTheatreTime      AS Tiempo_Total_Pabellon_Min,

    -- === TIEMPOS REALES ===
    RBOP.RBOP_TimeSurgery               AS Hora_Cirugia_Real,
    RBOP.RBOP_ProcedureStartTime        AS Hora_Inicio_Proc,
    RBOP.RBOP_ProcedureEndTime          AS Hora_Fin_Proc,
    RBOP.RBOP_DateArrived               AS Fecha_Llegada,
    RBOP.RBOP_TimeArrived               AS Hora_Llegada,

    -- === PREOPERATORIO ===
    RBOP.RBOP_PreopDate                 AS Fecha_PreOp,
    RBOP.RBOP_PreopTestDone             AS Examenes_PreOp_Hechos,
    RBOP.RBOP_PreOpCheckDone            AS Chequeo_PreOp_Hecho,
    RBOP.RBOP_RequiresFasting           AS Requiere_Ayuno,

    -- === REQUERIMIENTOS ESPECIALES ===
    RBOP.RBOP_BloodRequired             AS Requiere_Sangre,
    RBOP.RBOP_ICUBedRequired            AS Requiere_UCI,
    RBOP.RBOP_ProstheticsRequired       AS Requiere_Protesis,
    RBOP.RBOP_Infect                    AS Paciente_Infectado,
    RBOP.RBOP_MortalityRiskPerc         AS Riesgo_Mortalidad_Pct,

    -- === PABELLÓN / RECURSO ===
    RBOP.RBOP_Resource_DR               AS ID_Pabellon,
    RBOP.RBOP_Loc_DR                    AS ID_Ubicacion,

    -- === POSTOPERATORIO ===
    RBOP.RBOP_FollowUpRequired          AS Seguimiento_Requerido,
    RBOP.RBOP_FollowUpDone              AS Seguimiento_Hecho,
    RBOP.RBOP_EstimEpisLOS              AS Estadia_Estimada_Dias,

    -- === OBSERVACIONES ===
    RBOP.RBOP_Remarks                   AS Observaciones,

    -- === AUDITORÍA ===
    RBOP.RBOP_CreateDate                AS Fecha_Creacion,
    RBOP.RBOP_UpdateDate                AS Fecha_Actualizacion

FROM SQLUser.RB_OperatingRoom RBOP
    JOIN SQLUser.PA_Adm Adm
        ON RBOP.RBOP_PAADM_DR = Adm.PAADM_RowId
    JOIN SQLUser.PA_PatMas Pat
        ON Adm.PAADM_PAPMI_DR = Pat.PAPMI_RowId
WHERE RBOP.RBOP_DateOper >= '2025-01-01'
ORDER BY RBOP.RBOP_DateOper DESC, RBOP.RBOP_TimeOper ASC;


-- ============================================================================
-- QUERY 2: PROTOCOLO ANESTÉSICO COMPLETO
-- Uso: Detalle del acto anestésico con timeline perioperatorio
-- ============================================================================
SELECT TOP 200
    -- === IDENTIFICACIÓN ===
    ANA.ANA_RowId                       AS ID_Anestesia,
    ANA.ANA_No                          AS Num_Anestesia,

    -- === ESTADO ANESTESIA ===
    ANA.ANA_Status                      AS Estado_Anestesia,

    -- === PACIENTE ===
    Pat.PAPMI_ID                        AS RUT_Paciente,
    Pat.PAPMI_Name                      AS Apellido_Paterno,
    Pat.PAPMI_Name2                     AS Nombre_Paciente,
    Adm.PAADM_ADMNo                    AS Num_Admision,
    Adm.PAADM_Type                     AS Tipo_Episodio,

    -- === FECHA Y MÉTODO ===
    ANA.ANA_Date                        AS Fecha_Anestesia,
    ANA.ANA_AnaestMethods               AS Metodos_Anestesia,

    -- === PROFESIONALES ===
    ANA.ANA_Anaesthetist_DR             AS ID_Anestesiologo,
    ANA.ANA_Supervisor_DR               AS ID_Supervisor,
    ANA.ANA_ORAnaNurse_DR               AS ID_Enfermera_Anest,
    ANA.ANA_PACUAnaNurse_DR             AS ID_Enfermera_PACU,

    -- === PRE-EVALUACIÓN ANESTÉSICA ===
    ANA.ANA_PreAnaAssessDate            AS Fecha_Evaluacion_PreAnest,
    ANA.ANA_PreAnaAssessMalampatiScore  AS Score_Mallampati,
    ANA.ANA_PreAnaAssessHistory         AS Historia_PreAnest,
    ANA.ANA_PreAnaAssessCardiovasResp   AS Eval_Cardiovascular_Resp,
    ANA.ANA_PreAnaAssessAirwayDent      AS Eval_Via_Aerea_Dental,
    ANA.ANA_PreAnaAssessPlan            AS Plan_Anestesico,
    ANA.ANA_PreAnaAssessInfAnaRisk      AS Riesgo_Anestesico,

    -- === TIMELINE PERIOPERATORIO COMPLETO ===
    -- 1. Llamada al paciente
    ANA.ANA_PatCallDate                 AS T01_Llamada_Fecha,
    ANA.ANA_PatCallTime                 AS T01_Llamada_Hora,
    -- 2. Preparación del pabellón
    ANA.ANA_OTRoomPrepDate              AS T02_PrepPabellon_Fecha,
    ANA.ANA_OTRoomPrepTime              AS T02_PrepPabellon_Hora,
    -- 3. Entrada al área
    ANA.ANA_AreaInDate                  AS T03_EntradaArea_Fecha,
    ANA.ANA_AreaInTime                  AS T03_EntradaArea_Hora,
    -- 4. Sala PreOp
    ANA.ANA_PreOpRoomInDate             AS T04_SalaPreOp_Fecha,
    ANA.ANA_PreOpRoomInTime             AS T04_SalaPreOp_Hora,
    -- 5. Entrada a pabellón
    ANA.ANA_TheatreInDate               AS T05_EntradaPabellon_Fecha,
    ANA.ANA_TheatreInTime               AS T05_EntradaPabellon_Hora,
    -- 6. Inicio anestesia
    ANA.ANA_AnaStartTime                AS T06_InicioAnest_Hora,
    -- 7. Paciente listo post-inducción
    ANA.ANA_PatAnaInducDate             AS T07_PostInduccion_Fecha,
    ANA.ANA_PatAnaInducTime             AS T07_PostInduccion_Hora,
    -- 8. Inicio cirugía
    ANA.ANA_SurgStartTime               AS T08_InicioCirugia_Hora,
    -- 9. Fin cirugía
    ANA.ANA_SurgFinishTime              AS T09_FinCirugia_Hora,
    ANA.ANA_Surgery_Duration            AS Duracion_Cirugia,
    -- 10. Fin anestesia
    ANA.ANA_AnaFinishTime               AS T10_FinAnest_Hora,
    ANA.ANA_Anest_Duration              AS Duracion_Anestesia,
    -- 11. Paciente despierta
    ANA.ANA_PatAwakeDate                AS T11_Despertar_Fecha,
    ANA.ANA_PatAwakeTime                AS T11_Despertar_Hora,
    -- 12. Extubación
    ANA.ANA_ExtubTime                   AS T12_Extubacion_Hora,
    ANA.ANA_ExtubDone                   AS Extubacion_Realizada,
    -- 13. Salida de pabellón
    ANA.ANA_TheatreOutDate              AS T13_SalidaPabellon_Fecha,
    ANA.ANA_TheatreOutTime              AS T13_SalidaPabellon_Hora,
    -- 14. PACU (Recuperación)
    ANA.ANA_PACU_StartDate              AS T14_InicioPACU_Fecha,
    ANA.ANA_PACU_StartTime              AS T14_InicioPACU_Hora,
    ANA.ANA_PACU_FinishDate             AS T15_FinPACU_Fecha,
    ANA.ANA_PACU_FinishTime             AS T15_FinPACU_Hora,
    ANA.ANA_PACU_ReadyLeaveDate         AS T16_ListoAlta_Fecha,
    ANA.ANA_PACU_ReadyLeaveTime         AS T16_ListoAlta_Hora,
    -- 15. Salida del área
    ANA.ANA_AreaOutDate                 AS T17_SalidaArea_Fecha,
    ANA.ANA_AreaOutTime                 AS T17_SalidaArea_Hora,
    -- 16. Limpieza
    ANA.ANA_StartCleaningDate           AS T18_InicioLimpieza_Fecha,
    ANA.ANA_StartCleaningTime           AS T18_InicioLimpieza_Hora,
    ANA.ANA_EndCleaningDate             AS T19_FinLimpieza_Fecha,
    ANA.ANA_EndCleaningTime             AS T19_FinLimpieza_Hora,

    -- === TIEMPO TOTAL ===
    ANA.ANA_TotalOTRoomTime             AS Tiempo_Total_Pabellon_Min,

    -- === VIA AÉREA ===
    ANA.ANA_AirwayMgtComments           AS Via_Aerea_Comentarios,
    ANA.ANA_AirwayMgtPEEP               AS PEEP,

    -- === BALANCE HÍDRICO ===
    ANA.ANA_AmtBloodLoss                AS Perdida_Sangre_ml,
    ANA.ANA_AmtBloodTranfused           AS Sangre_Transfundida_ml,
    ANA.ANA_AmtFluidInfused             AS Liquidos_Infundidos_ml,
    ANA.ANA_AmtUrineOutput              AS Diuresis_ml,
    ANA.ANA_Total_Input                 AS Total_Ingreso_ml,
    ANA.ANA_Total_Output                AS Total_Egreso_ml,

    -- === COMPLICACIONES / RESULTADO ===
    ANA.ANA_CompComments                AS Complicaciones_Comentarios,
    ANA.ANA_PostOperInstructions        AS Instrucciones_PostOp,
    ANA.ANA_Notes                       AS Notas_Anestesia,

    -- === PABELLÓN ===
    ANA.ANA_RBOperatingRoom_DR          AS ID_Booking_Pabellon,

    -- === AUDITORÍA ===
    ANA.ANA_UpdateDate                  AS Fecha_Actualizacion,
    ANA.ANA_RecReviewed                 AS Registro_Revisado

FROM SQLUser.OR_Anaesthesia ANA
    JOIN SQLUser.PA_Adm Adm
        ON ANA.ANA_PAADM_ParRef = Adm.PAADM_RowId
    JOIN SQLUser.PA_PatMas Pat
        ON Adm.PAADM_PAPMI_DR = Pat.PAPMI_RowId
WHERE ANA.ANA_Date >= '2025-01-01'
ORDER BY ANA.ANA_Date DESC, ANA.ANA_AnaStartTime ASC;


-- ============================================================================
-- QUERY 3: DETALLE OPERACIÓN QUIRÚRGICA (Protocolo Operatorio)
-- Uso: Registro detallado de la operación con estados de protocolo
-- ============================================================================
SELECT TOP 200
    -- === IDENTIFICACIÓN ===
    ANAOP.ANAOP_RowId                   AS ID_Operacion,
    ANAOP.ANAOP_No                      AS Num_Operacion,
    ANAOP.ANAOP_Par_Ref                 AS ID_Anestesia_Padre,

    -- === ESTADOS DEL PROTOCOLO QUIRÚRGICO ===
    ANAOP.ANAOP_Status                  AS Estado_Operacion,
    ANAOP.ANAOP_StatePPP_DR             AS ID_Estado_PPP,

    -- === PACIENTE ===
    Pat.PAPMI_ID                        AS RUT_Paciente,
    Pat.PAPMI_Name                      AS Apellido_Paterno,
    Pat.PAPMI_Name2                     AS Nombre_Paciente,
    Adm.PAADM_ADMNo                    AS Num_Admision,

    -- === TIPO Y CATEGORÍA ===
    ANAOP.ANAOP_OperType                AS Tipo_Operacion,
    ANAOP.ANAOP_DaySurgery              AS Cirugia_Ambulatoria,
    ANAOP.ANAOP_EffectiveElective       AS Electiva_Efectiva,
    ANAOP.ANAOP_Procedure               AS Procedimiento_Texto,
    ANAOP.ANAOP_Details                 AS Detalles_Operacion,
    ANAOP.ANAOP_ProceduralDetails       AS Detalles_Procedurales,

    -- === EQUIPO QUIRÚRGICO ===
    ANAOP.ANAOP_Surgeon_DR              AS ID_Cirujano,
    ANAOP.ANAOP_SurgeonAssist_DR        AS ID_Cirujano_Asistente,
    ANAOP.ANAOP_SecondSurgeon_DR        AS ID_Segundo_Cirujano,
    ANAOP.ANAOP_Anaesthetist_DR         AS ID_Anestesiologo,
    ANAOP.ANAOP_Circul_Nurse_DR         AS ID_Enfermera_Circulante,

    -- === DIAGNÓSTICOS ===
    ANAOP.ANAOP_PreOPDiagnosis          AS Diagnostico_PreOp,
    ANAOP.ANAOP_PostOPDiagnosisDiff     AS Diagnostico_PostOp,

    -- === TIEMPOS DE LA OPERACIÓN ===
    ANAOP.ANAOP_OpStartDate             AS Fecha_Inicio_OP,
    ANAOP.ANAOP_OpStartTime             AS Hora_Inicio_OP,
    ANAOP.ANAOP_OpEndDate               AS Fecha_Fin_OP,
    ANAOP.ANAOP_OpEndTime               AS Hora_Fin_OP,
    ANAOP.ANAOP_TheatreInDate           AS Fecha_Entrada_Pabellon,
    ANAOP.ANAOP_TheatreInTime           AS Hora_Entrada_Pabellon,
    ANAOP.ANAOP_TheatreOutDate          AS Fecha_Salida_Pabellon,
    ANAOP.ANAOP_TheatreOutTime          AS Hora_Salida_Pabellon,
    ANAOP.ANAOP_AreaInDate              AS Fecha_Entrada_Area,
    ANAOP.ANAOP_AreaInTime              AS Hora_Entrada_Area,
    ANAOP.ANAOP_AreaOutDate             AS Fecha_Salida_Area,
    ANAOP.ANAOP_AreaOutTime             AS Hora_Salida_Area,

    -- === CONTEO QUIRÚRGICO (Surgical Count Protocol) ===
    ANAOP.ANAOP_InitialCountCorrect     AS Conteo_Inicial_Correcto,
    ANAOP.ANAOP_FinalCountCorrect       AS Conteo_Final_Correcto,
    ANAOP.ANAOP_CountedItems            AS Items_Contados,
    ANAOP.ANAOP_SurgCountNote           AS Nota_Conteo_Quirurgico,
    ANAOP.ANAOP_SurgeonNotified         AS Cirujano_Notificado,

    -- === PROTOCOLO DE HERIDA ===
    ANAOP.ANAOP_SurgicalWoundStatus     AS Estado_Herida_Quirurgica,
    ANAOP.ANAOP_Closure                 AS Cierre_Herida,
    ANAOP.ANAOP_DrainsInSitu            AS Drenajes_In_Situ,
    ANAOP.ANAOP_ProthesisUsed           AS Protesis_Utilizada,
    ANAOP.ANAOP_PathologySent           AS Patologia_Enviada,
    ANAOP.ANAOP_BiopsyPerformed         AS Biopsia_Realizada,
    ANAOP.ANAOP_XRayTaken               AS Radiografia_Tomada,

    -- === COMPLICACIONES ===
    ANAOP.ANAOP_OperationComplication    AS Complicacion_Operatoria,
    ANAOP.ANAOP_Findings                AS Hallazgos,
    ANAOP.ANAOP_CancelReason            AS Razon_Cancelacion,

    -- === POST-OPERATORIO ===
    ANAOP.ANAOP_PostOperInstructions    AS Instrucciones_PostOp,
    ANAOP.ANAOP_PostFollowUpApptReq     AS Seguimiento_Requerido,
    ANAOP.ANAOP_PostFollowUpApptDate    AS Fecha_Seguimiento,
    ANAOP.ANAOP_PostSpecToPathology     AS Muestra_A_Patologia,

    -- === NOTAS ===
    ANAOP.ANAOP_Notes                   AS Notas_Operacion,

    -- === AUDITORÍA ===
    ANAOP.ANAOP_CreatedDate             AS Fecha_Creacion,
    ANAOP.ANAOP_CreatedTime             AS Hora_Creacion,
    ANAOP.ANAOP_UpdateDate              AS Fecha_Actualizacion

FROM SQLUser.OR_Anaest_Operation ANAOP
    JOIN SQLUser.OR_Anaesthesia ANA
        ON ANAOP.ANAOP_Par_Ref = ANA.ANA_RowId
    JOIN SQLUser.PA_Adm Adm
        ON ANA.ANA_PAADM_ParRef = Adm.PAADM_RowId
    JOIN SQLUser.PA_PatMas Pat
        ON Adm.PAADM_PAPMI_DR = Pat.PAPMI_RowId
WHERE ANA.ANA_Date >= '2025-01-01'
ORDER BY ANAOP.ANAOP_OpStartDate DESC, ANAOP.ANAOP_OpStartTime ASC;


-- ============================================================================
-- QUERY 4: VISTA UNIFICADA - BOOKING + ANESTESIA + OPERACIÓN + PACIENTE
-- Uso: Query maestro que une todo el flujo perioperatorio
-- ============================================================================
SELECT TOP 200
    -- === PACIENTE ===
    Pat.PAPMI_ID                        AS RUT,
    Pat.PAPMI_Name                      AS Apellido,
    Pat.PAPMI_Name2                     AS Nombre,
    Pat.PAPMI_DOB                       AS Fecha_Nacimiento,
    Adm.PAADM_ADMNo                    AS Num_Admision,
    Adm.PAADM_Type                     AS Tipo_Episodio,

    -- === BOOKING (Programación) ===
    RBOP.RBOP_BookingNumber             AS Num_Reserva,
    RBOP.RBOP_DateOper                  AS Fecha_Programada,
    RBOP.RBOP_TimeOper                  AS Hora_Programada,
    RBOP.RBOP_Status                    AS Estado_Booking,
    CASE RBOP.RBOP_Status
        WHEN 'P' THEN 'Programado'
        WHEN 'A' THEN 'Admitido'
        WHEN 'I' THEN 'En Curso'
        WHEN 'C' THEN 'Completado'
        WHEN 'X' THEN 'Cancelado'
        WHEN 'S' THEN 'Suspendido'
        ELSE RBOP.RBOP_Status
    END                                 AS Estado_Booking_Desc,
    RBOP.RBOP_Procedure                 AS Procedimiento_Programado,
    RBOP.RBOP_DaySurgery                AS Cirugia_Ambulatoria,
    RBOP.RBOP_Arrived                   AS Paciente_Llego,
    RBOP.RBOP_CancelReason              AS Razon_Cancelacion_Booking,

    -- === ANESTESIA (Registro) ===
    ANA.ANA_Status                      AS Estado_Anestesia,
    ANA.ANA_Date                        AS Fecha_Anestesia,
    ANA.ANA_AnaestMethods               AS Metodo_Anestesia,
    ANA.ANA_AnaStartTime                AS Inicio_Anestesia,
    ANA.ANA_AnaFinishTime               AS Fin_Anestesia,
    ANA.ANA_Anest_Duration              AS Duracion_Anestesia,
    ANA.ANA_SurgStartTime               AS Inicio_Cirugia,
    ANA.ANA_SurgFinishTime              AS Fin_Cirugia,
    ANA.ANA_Surgery_Duration            AS Duracion_Cirugia,

    -- === TIMELINE CLAVE ===
    ANA.ANA_TheatreInTime               AS Hora_Entrada_Pabellon,
    ANA.ANA_TheatreOutTime              AS Hora_Salida_Pabellon,
    ANA.ANA_TotalOTRoomTime             AS Tiempo_Total_Pabellon_Min,
    ANA.ANA_PACU_StartTime              AS Inicio_PACU,
    ANA.ANA_PACU_FinishTime             AS Fin_PACU,
    ANA.ANA_PACU_ReadyLeaveTime         AS Listo_Alta_PACU,

    -- === OPERACIÓN (Protocolo Quirúrgico) ===
    ANAOP.ANAOP_Status                  AS Estado_Operacion,
    ANAOP.ANAOP_StatePPP_DR             AS ID_Estado_PPP,
    ANAOP.ANAOP_Procedure               AS Procedimiento_Realizado,
    ANAOP.ANAOP_OperType                AS Tipo_Operacion,
    ANAOP.ANAOP_PreOPDiagnosis          AS Diagnostico_PreOp,
    ANAOP.ANAOP_PostOPDiagnosisDiff     AS Diagnostico_PostOp,
    ANAOP.ANAOP_OpStartTime             AS Hora_Inicio_OP,
    ANAOP.ANAOP_OpEndTime               AS Hora_Fin_OP,

    -- === EQUIPO QUIRÚRGICO ===
    ANAOP.ANAOP_Surgeon_DR              AS ID_Cirujano,
    ANAOP.ANAOP_SurgeonAssist_DR        AS ID_Cirujano_Asistente,
    ANAOP.ANAOP_Circul_Nurse_DR         AS ID_Enfermera_Circulante,
    ANA.ANA_Anaesthetist_DR             AS ID_Anestesiologo,

    -- === PROTOCOLOS DE SEGURIDAD ===
    ANAOP.ANAOP_InitialCountCorrect     AS Conteo_Inicial_OK,
    ANAOP.ANAOP_FinalCountCorrect       AS Conteo_Final_OK,
    ANAOP.ANAOP_SurgicalWoundStatus     AS Estado_Herida,
    ANAOP.ANAOP_DrainsInSitu            AS Drenajes,

    -- === BALANCE HÍDRICO ===
    ANA.ANA_AmtBloodLoss                AS Perdida_Sangre_ml,
    ANA.ANA_AmtFluidInfused             AS Liquidos_ml,
    ANA.ANA_AmtBloodTranfused           AS Sangre_Transfundida_ml,

    -- === COMPLICACIONES ===
    ANAOP.ANAOP_OperationComplication    AS Complicacion_Op,
    ANA.ANA_CompComments                AS Complicacion_Anest,

    -- === NOTAS ===
    ANAOP.ANAOP_Notes                   AS Notas_Operacion,
    ANA.ANA_Notes                       AS Notas_Anestesia,
    ANAOP.ANAOP_PostOperInstructions    AS Instrucciones_PostOp

FROM SQLUser.RB_OperatingRoom RBOP
    JOIN SQLUser.PA_Adm Adm
        ON RBOP.RBOP_PAADM_DR = Adm.PAADM_RowId
    JOIN SQLUser.PA_PatMas Pat
        ON Adm.PAADM_PAPMI_DR = Pat.PAPMI_RowId
    LEFT JOIN SQLUser.OR_Anaesthesia ANA
        ON ANA.ANA_PAADM_ParRef = Adm.PAADM_RowId
    LEFT JOIN SQLUser.OR_Anaest_Operation ANAOP
        ON ANAOP.ANAOP_Par_Ref = ANA.ANA_RowId
WHERE RBOP.RBOP_DateOper >= '2025-01-01'
ORDER BY RBOP.RBOP_DateOper DESC, RBOP.RBOP_TimeOper ASC;


-- ============================================================================
-- QUERY 5: CATÁLOGO DE ESTADOS PPP (Referencia)
-- Uso: Listar todos los estados de protocolo disponibles
-- ============================================================================
SELECT TOP 100
    SPPP.SPPP_RowId                     AS ID_Estado,
    SPPP.SPPP_Code                      AS Codigo_Estado,
    SPPP.SPPP_Desc                      AS Descripcion_Estado,
    SPPP.SPPP_EpisodeTypes              AS Tipos_Episodio,
    SPPP.SPPP_Operations                AS Operaciones_Asociadas,
    SPPP.SPPP_EstTime                   AS Tiempo_Estimado,
    SPPP.SPPP_EstLOS                    AS Estadia_Estimada,
    SPPP.SPPP_RecoveryType              AS Tipo_Recuperacion,
    SPPP.SPPP_StartDate                 AS Fecha_Inicio_Vigencia,
    SPPP.SPPP_EndDate                   AS Fecha_Fin_Vigencia
FROM SQLUser.PAC_StatePPP SPPP
ORDER BY SPPP.SPPP_Code;


-- ============================================================================
-- QUERY 6: CATÁLOGO DE OPERACIONES (ORC_Operation)
-- Uso: Listar operaciones/procedimientos quirúrgicos disponibles
-- ============================================================================
SELECT TOP 200
    OPER.OPER_RowId                     AS ID_Operacion,
    OPER.OPER_Code                      AS Codigo_ICD,
    OPER.OPER_Desc                      AS Descripcion_Operacion,
    OPER.OPER_LongDescription           AS Descripcion_Larga,
    OPER.OPER_ICD10                     AS Codigo_ICD10,
    OPER.OPER_NationalCode              AS Codigo_Nacional,
    OPER.OPER_DaySurgery                AS Cirugia_Ambulatoria,
    OPER.OPER_DefaultEstimTime          AS Tiempo_Estimado_Default,
    OPER.OPER_LengthOfStay              AS Estadia_Estimada,
    OPER.OPER_DateActiveFrom            AS Vigente_Desde,
    OPER.OPER_ActiveDateTo              AS Vigente_Hasta,
    OPER.OPER_Valid                      AS Valido
FROM SQLUser.ORC_Operation OPER
WHERE OPER.OPER_Valid IS NULL OR OPER.OPER_Valid != 'N'
ORDER BY OPER.OPER_Code;
