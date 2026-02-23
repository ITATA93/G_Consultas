# questionnaire.QTCEEIEDQQ05

> Entrevista de Ingreso Equipo Derivador : Equipos y Familiares Que Efectuarán Visitas (Consignar Fecha 1ra Visita)

**Schema:** questionnaire
**Columnas:** 6
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Entrevista de Ingreso Equipo Derivador : Equipos y Familiares Que Efectuarán Visitas (Consignar Fecha 1ra Visita)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q05Q1 | varchar |  |  | SI | Equipos |
| Q05Q2 | varchar |  |  | SI | Familiares |
| Q05Q3 | date |  |  | SI | Fechas |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*