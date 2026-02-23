-- ============================================
-- REGISTRAR QUERY CAPRINI EN METADATA SIDRA
-- Tabla destino: ALMA_Meta.CFG_Queries
-- ============================================

DELETE FROM ALMA_Meta.CFG_Queries 
WHERE SchemaDestino = 'ALMA_Reportes' AND TablaDestino = 'CAL_RiesgoETE';

INSERT INTO ALMA_Meta.CFG_Queries
(
    SchemaDestino, 
    TablaDestino, 
    TipoTabla, 
    ServidorOrigen, 
    BaseDatosOrigen, 
    TablaOrigen, 
    QueryExtraccion, 
    Descripcion, 
    FrecuenciaSinc
)
VALUES
(
    'ALMA_Reportes',
    'CAL_RiesgoETE',
    'CAL',
    'IRIS',
    'LIVE-CLOV',
    'questionnaire.QTCEEVRIEST',
    'SELECT Q.ID, Pat.PAPMI_No, Pat.PAPMI_Name, Pat.PAPMI_Name2, Adm.PAADM_AdmNo, Adm.PAADM_AdmDate, Adm.PAADM_AdmTime, Loc.CTLOC_Desc, Q.QUESDate, Q.QUESTime, SSU.SSUSR_Name, Q.Q01, Q.Q02, Q.Q03, Q.Q04, Q.Q05, Q.Q06, Q.QUESScore FROM questionnaire.QTCEEVRIEST Q JOIN SQLUser.PA_Adm Adm ON Q.QUESPAAdmDR = Adm.PAADM_RowId JOIN SQLUser.PA_PatMas Pat ON Adm.PAADM_PAPMI_DR = Pat.PAPMI_RowId LEFT JOIN SQLUser.CT_Loc Loc ON Adm.PAADM_DepCode_DR = Loc.CTLOC_RowId LEFT JOIN SQLUser.SS_User SSU ON Q.QUESUserDR = SSU.SSUSR_RowId WHERE Q.QUESDate >= (CURRENT_DATE - 1)',
    'Reporte de Riesgo Tromboembolico basado en formulario Caprini (QTCEEVRIEST). Sincronizacion diaria de ultimas 24hrs.',
    'Diaria'
);

-- Verificacion
SELECT * FROM ALMA_Meta.CFG_Queries WHERE TablaDestino = 'CAL_RiesgoETE';
