---
depends_on: []
impacts: []
---

# Changelog — G_Consultas

All notable changes to this project will be documented in this file.
Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]

### Added

- `scripts/crear_schema_consultor_sidra.py` — DDL para schema ALMA_Consultor en SIDRA-TEST
  con 5 tablas (IC_Llamado, Cx_Pabellon, Cx_Endoscopia, Cx_Menor, Procedimientos)
  y vista clinica consolidada V_Resumen_Clinico
- `scripts/etl_consultor_alma_sidra.py` — ETL ALMA→SIDRA: extrae IC de llamado,
  cruza cirugias/procedimientos del mismo medico en ventana 48h, carga a SIDRA-TEST.
  Incluye codigos FONASA, procedimientos secundarios, horas post-IC, estados legibles
- `scripts/exportar_catalogos_alma.py` — Exporta catalogos ALMA a SQLite local
- `Consultas_live/rpt_consultoria_llamado.py` — Reporte standalone IC llamado (ALMA→CSV)
- `herramientas/python/dic_local.py` — Motor diccionario local SQLite
- `docs/research/flujo_interconsultas_alma.md` — Investigacion completa del flujo
  de interconsultas internas, consultorias de llamado, teleconsultas y evaluaciones
- `docs/research/catalogos/` — Exportaciones CSV de catalogos ALMA:
  - `interconsultas_internas_hova.csv` (44 items)
  - `consultorias_llamado_hova.csv` (13 items)
  - `teleconsultas.csv` (48 items)
  - `evaluaciones.csv` (35 items)
  - `grupos_interconsulta.csv` (15 grupos receptores)
  - `estados_orden.csv` (13 estados OEC_OrderStatus)
  - `estados_solicitud_ic.csv` (3 estados PAC_RequestStatus)
  - `metodos_contacto_ic.csv` (3 metodos PAC_ContMethod)
- `tests/test_conexion_alma.py` — Test basico de conexion a ALMA/IRIS
- `tests/verify_enquiry_contact_ic.py` — Verificacion PA_EnquiryContact para IC
- `tests/verify_ordstatus_catalog.py` — Resolucion catalogo OEC_OrderStatus
- `tests/test_queries_consultor.py` — Test 8 queries Parte 3 paquete DBA contra SIDRA-TEST
- `exports/paquete_dba_consultor.sql` — Paquete completo para DBA: queries ALMA, DDL SIDRA,
  consultas clinicas (3 partes)
- `exports/demo_consultor_sidra.sql` — Demo rapido de queries sobre datos ya cargados

### Discovered

- Flujo IC: OE_OrdItem (HOVA*) → OE_OrdItem2.ITM2_Group_DR → SS_Group → MR_Encounter
- Decorator regional `Region_CLXX_Misc_User.OEOrdItem` (GES, verificacion, secuencia)
- `COEORI_QuestID` existe pero nunca se pobla — respuesta es encuentro estandar EPR
- `PA_Consultation` y `PA_ConsultationLink` vacias en esta instancia
- `epr.TaskList` no se usa para interconsultas (solo alertas GES y temperatura)
- 15 grupos de usuario receptores mapeados (incluye grupo 48: "Medico Interconsultor")
- **PA_EnquiryContact** es la tabla del formulario "Datos de Contacto" IC (2,103 registros)
- Transicion de estados IC: Inactivo(5) → Solicitado(12) → Ejecutado(3) via OE_OrdStatus
- Catalogo OEC_OrderStatus: 13 estados de orden mapeados
- PAC_RequestStatus: Asignada / En Proceso / Finalizada
- PAC_ContMethod: WhatsApp / Telefonico / Correo Electronico
- UI: componente `Region.CLXX.Model.EPVisitNumber.ClinicWorkList.LTInterconsultasInternas`
- Menus IC: CLXX.ICInternasSol (sin asignar), CLXX.ICInternasAsig (asignadas)

### Fixed

- `.env` actualizado con credenciales reales desde legacy AG_Consultas

### Notes

- Governance audit: docs/TODO.md verified
- README.md enhanced with architecture and usage docs
- Gemini CLI integration validated

## [1.0.0] — 2026-02-23

### Added
- Full GEN_OS mirror infrastructure migrated from AG_Consultas.
- Multi-vendor dispatch: .subagents/, .claude/, .codex/, .gemini/, .agent/.
- Governance standards: docs/standards/.
- CI/CD workflows: .github/workflows/.
- All domain content preserved from AG_Consultas.
