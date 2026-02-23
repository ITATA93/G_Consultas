# Guía de Uso del Sistema de Mapeo TrakCare/ALMA

> Guía completa para usar el sistema de mapeo y construcción de consultas SQL seguras

---

## 📑 Tabla de Contenidos

1. [Introducción](#introducción)
2. [Configuración Inicial](#configuración-inicial)
3. [Uso de Agentes Claude Code](#uso-de-agentes-claude-code)
4. [Construcción de Consultas Paso a Paso](#construcción-de-consultas-paso-a-paso)
5. [Casos de Uso Comunes](#casos-de-uso-comunes)
6. [Validación de Consultas](#validación-de-consultas)
7. [Resolución de Problemas](#resolución-de-problemas)
8. [Mejores Prácticas](#mejores-prácticas)

---

## 📖 Introducción

Este sistema te permite:
- ✅ Mapear la estructura de la base de datos TrakCare/ALMA
- ✅ Construir consultas SQL de forma segura
- ✅ Responder a necesidades clínicas y administrativas
- ✅ Validar consultas antes de ejecutarlas
- ✅ Documentar y compartir consultas

**IMPORTANTE**: Este sistema está diseñado para **SOLO LECTURA**. Nunca podrás modificar, borrar o actualizar datos.

---

## ⚙️ Configuración Inicial

### Paso 1: Verificar Instalación de Herramientas

#### DbVisualizer Pro
```bash
# Verificar que existe
cd c:\_Consultas\DbVisualizer_Pro_10.0.20_x64_crackzsoft.com
```

#### Python (para scripts de validación)
```bash
python --version
# Debe ser Python 3.7+
```

#### Claude Code (para agentes)
```bash
claude --version
```

### Paso 2: Configurar Conexión a Base de Datos

1. Abrir DbVisualizer
2. Ir a **Database → Create Database Connection**
3. Configurar:
   - **Name**: ALMA IRIS
   - **Driver**: InterSystems IRIS JDBC
   - **Database Server**: 10.63.180.25
   - **Database Port**: 51773
   - **Database**: LIVE-CLOV
   - **Database Userid**: (ver `credentials/alma_iris.txt`)
   - **Database Password**: (ver `credentials/alma_iris.txt`)

4. Click **Connect**
5. Si conecta exitosamente, ver en panel izquierdo: **ALMA IRIS → LIVE-CLOV → SQLUser**

### Paso 3: Verificar Acceso a Documentación

```bash
cd c:\_Consultas
# Verificar que existen
ls datos_alma/docs/
ls docs/guias/
ls .claude/agents/
```

---

## 🤖 Uso de Agentes Claude Code

Este sistema incluye 4 agentes especializados. Aquí está cómo usarlos:

### Agente 1: Mapeo de Base de Datos

**Cuándo usarlo**: Cuando necesites entender la estructura de tablas

**Comandos**:
```bash
# En Claude Code
@mapeo_trakcare ¿Qué tablas contienen datos de pacientes?
@mapeo_trakcare ¿Cómo se relaciona PA_Adm con PA_Person?
@mapeo_trakcare Explica el módulo de órdenes médicas (OE_)
```

**Ejemplo de salida**:
```markdown
## Tabla: PA_Adm (Administración de Pacientes)

**Propósito**: Registra episodios de admisión/ingreso

**Columnas clave**:
- PAADM_RowId: Clave primaria
- PAADM_PAPMI_DR: FK → PA_PatMas (paciente)
- PAADM_AdmDate: Fecha de ingreso
- PAADM_DischgDate: Fecha de alta

**Relaciones**:
- Padre: PA_PatMas (un paciente tiene muchos episodios)
- Hijos: MR_Adm (registro clínico), OE_Order (órdenes)
```

---

### Agente 2: Constructor de Consultas

**Cuándo usarlo**: Cuando necesites generar una consulta SQL

**Comandos**:
```bash
@constructor_consultas Necesito listar pacientes hospitalizados hoy
@constructor_consultas Dame las órdenes de laboratorio pendientes
@constructor_consultas Consulta de pacientes diabéticos en tratamiento
```

**Ejemplo de salida**:
```sql
-- =================================================================
-- CONSULTA: Pacientes Hospitalizados Hoy
-- PROPÓSITO: Listar todos los pacientes actualmente hospitalizados
-- =================================================================

SELECT TOP 100
    PA.PAADM_ADMNo AS NumeroEpisodio,
    P.PAPER_Name AS NombrePaciente,
    PA.PAADM_AdmDate AS FechaIngreso,
    L.CTLOC_Desc AS Servicio
FROM SQLUser.PA_Adm PA
INNER JOIN SQLUser.PA_PatMas PM ON PA.PAADM_PAPMI_DR = PM.PAPMI_RowId
INNER JOIN SQLUser.PA_Person P ON PM.PAPMI_PAPER_DR = P.PAPER_RowId
LEFT JOIN SQLUser.CT_Loc L ON PA.PAADM_CTLOC_DR = L.CTLOC_RowId
WHERE PA.PAADM_Type = 'I'
  AND PA.PAADM_DischgDate IS NULL
ORDER BY PA.PAADM_AdmDate DESC;
```

---

### Agente 3: Análisis Clínico

**Cuándo usarlo**: Cuando necesites traducir términos clínicos a técnicos

**Comandos**:
```bash
@analisis_clinico ¿Dónde se almacena la ficha de admisión?
@analisis_clinico ¿Qué significa PAADM_DRGCode?
@analisis_clinico Mapea el formulario de evolución médica
```

**Ejemplo de salida**:
```markdown
### Ficha de Admisión - Mapeo a BD

**Formulario Clínico** → **Tablas en BD**

1. **Datos de Identificación**
   - Nombre completo → PA_Person.PAPER_Name
   - RUT → PA_Person.PAPER_ID
   - Fecha de nacimiento → PA_Person.PAPER_DOB

2. **Datos del Episodio**
   - Número de episodio → PA_Adm.PAADM_ADMNo
   - Fecha de ingreso → PA_Adm.PAADM_AdmDate
   - Tipo de ingreso → PA_Adm.PAADM_Type

3. **Datos Administrativos**
   - Previsión → CT_Payor (vía FK)
   - Servicio → CT_Loc (vía FK)
   - Médico tratante → CT_CareProv (vía FK)
```

---

### Agente 4: Documentador

**Cuándo usarlo**: Cuando necesites documentar una tabla o consulta

**Comandos**:
```bash
@documentador Documenta la tabla PA_Adm
@documentador Genera diagrama ER del módulo MR_
@documentador Crea diccionario de OE_Order
```

---

## 🔨 Construcción de Consultas Paso a Paso

### Metodología de 7 Pasos

#### Paso 1: Identificar la Necesidad

**Pregúntate**:
- ¿Qué información necesito?
- ¿Es para un paciente específico o un grupo?
- ¿Qué rango de fechas?
- ¿Necesito datos en tiempo real o históricos?

**Ejemplo**: "Necesito saber qué pacientes están hospitalizados actualmente en el servicio de Medicina Interna"

---

#### Paso 2: Identificar Tabla Ancla

Según tu necesidad, elige la tabla principal:

| Necesidad | Tabla Ancla |
|-----------|-------------|
| Datos de pacientes | PA_Person, PA_PatMas |
| Episodios/ingresos | PA_Adm |
| Órdenes médicas | OE_Order |
| Diagnósticos | MR_Diagnos |
| Resultados laboratorio | LB_Result |
| Cirugías | OR_Operation |

**Para nuestro ejemplo**: `PA_Adm` (porque buscamos episodios activos)

---

#### Paso 3: Mapear Relaciones

Identifica qué otras tablas necesitas:

```
Necesito:
- Nombre del paciente → PA_Person
- Servicio → CT_Loc

Relaciones:
PA_Adm → PA_PatMas → PA_Person  (datos del paciente)
PA_Adm → CT_Loc                 (servicio)
```

**Diagrama**:
```
PA_Adm (ancla)
  ├─> PA_PatMas (vía PAADM_PAPMI_DR)
  │     └─> PA_Person (vía PAPMI_PAPER_DR)
  └─> CT_Loc (vía PAADM_CTLOC_DR)
```

---

#### Paso 4: Construir SELECT

```sql
SELECT TOP 100
    -- Identificadores
    PA.PAADM_ADMNo AS NumeroEpisodio,
    PM.PAPMI_No AS NumeroFicha,

    -- Datos del paciente
    P.PAPER_Name AS NombrePaciente,
    P.PAPER_Name2 AS ApellidoPaterno,

    -- Datos de admisión
    PA.PAADM_AdmDate AS FechaIngreso,
    L.CTLOC_Desc AS Servicio
```

---

#### Paso 5: Construir JOINs

**Regla**: `TablaHija.COLUMNA_DR = TablaPadre.TABLA_RowId`

```sql
FROM SQLUser.PA_Adm AS PA

-- Relación con Maestro de Pacientes
INNER JOIN SQLUser.PA_PatMas AS PM
    ON PA.PAADM_PAPMI_DR = PM.PAPMI_RowId

-- Relación con Datos Personales
INNER JOIN SQLUser.PA_Person AS P
    ON PM.PAPMI_PAPER_DR = P.PAPER_RowId

-- Relación con Ubicación/Servicio
LEFT JOIN SQLUser.CT_Loc AS L
    ON PA.PAADM_CTLOC_DR = L.CTLOC_RowId
```

---

#### Paso 6: Construir WHERE

```sql
WHERE
    -- Solo episodios de tipo Inpatient (hospitalizados)
    PA.PAADM_Type = 'I'

    -- Solo episodios sin alta (activos)
    AND PA.PAADM_DischgDate IS NULL

    -- Solo servicio de Medicina Interna
    AND L.CTLOC_Desc LIKE '%Medicina Interna%'
```

---

#### Paso 7: Ordenar y Documentar

```sql
ORDER BY PA.PAADM_AdmDate DESC;

-- NOTAS:
-- - Muestra máximo 100 registros
-- - Ordenado por fecha de ingreso (más recientes primero)
-- - PAADM_Type = 'I' significa Inpatient (hospitalizado)
```

---

### Consulta Completa Final

```sql
-- =================================================================
-- CONSULTA: Pacientes Hospitalizados en Medicina Interna
-- PROPÓSITO: Listar pacientes actualmente hospitalizados en MI
-- TABLAS: PA_Adm, PA_PatMas, PA_Person, CT_Loc
-- FECHA: 2026-01-25
-- LÍMITE: TOP 100 registros
-- =================================================================

SELECT TOP 100
    -- Identificadores
    PA.PAADM_ADMNo AS NumeroEpisodio,
    PM.PAPMI_No AS NumeroFicha,

    -- Datos del paciente
    P.PAPER_Name AS NombrePaciente,
    P.PAPER_Name2 AS ApellidoPaterno,

    -- Datos de admisión
    PA.PAADM_AdmDate AS FechaIngreso,
    L.CTLOC_Desc AS Servicio

FROM SQLUser.PA_Adm AS PA

-- Relación con Maestro de Pacientes
INNER JOIN SQLUser.PA_PatMas AS PM
    ON PA.PAADM_PAPMI_DR = PM.PAPMI_RowId

-- Relación con Datos Personales
INNER JOIN SQLUser.PA_Person AS P
    ON PM.PAPMI_PAPER_DR = P.PAPER_RowId

-- Relación con Ubicación/Servicio
LEFT JOIN SQLUser.CT_Loc AS L
    ON PA.PAADM_CTLOC_DR = L.CTLOC_RowId

WHERE
    -- Solo episodios de tipo Inpatient (hospitalizados)
    PA.PAADM_Type = 'I'

    -- Solo episodios sin alta (activos)
    AND PA.PAADM_DischgDate IS NULL

    -- Solo servicio de Medicina Interna
    AND L.CTLOC_Desc LIKE '%Medicina Interna%'

ORDER BY PA.PAADM_AdmDate DESC;

-- NOTAS:
-- - Muestra máximo 100 registros
-- - Ordenado por fecha de ingreso (más recientes primero)
-- - PAADM_Type = 'I' significa Inpatient (hospitalizado)
-- - DischgDate NULL significa que aún no ha sido dado de alta
```

---

## 📋 Casos de Uso Comunes

### Caso 1: Censo Hospitalario Actual

**Pregunta clínica**: "¿Cuántos pacientes tengo hospitalizados ahora?"

**Tabla ancla**: PA_Adm

**Filtros clave**:
- `PAADM_Type = 'I'` (Inpatient)
- `PAADM_DischgDate IS NULL` (sin alta)

**Ver consulta completa**: `consultas/clinicas/censo_hospitalario.sql`

---

### Caso 2: Altas del Día

**Pregunta clínica**: "¿Qué pacientes fueron dados de alta hoy?"

**Tabla ancla**: PA_Adm

**Filtros clave**:
- `CAST(PAADM_DischgDate AS DATE) = CAST(GETDATE() AS DATE)`

**Ver consulta completa**: `consultas/clinicas/altas_del_dia.sql`

---

### Caso 3: Órdenes de Laboratorio Pendientes

**Pregunta clínica**: "¿Qué exámenes de laboratorio están pendientes?"

**Tabla ancla**: OE_Order, OE_OrdItem

**Filtros clave**:
- `OEORD_ItemCat = 'LAB'`
- `OEORI_ItemStatus != 'Completed'`
- `OEORI_ItemStatus != 'Cancelled'`

**Ver consulta completa**: `consultas/clinicas/ordenes_lab_pendientes.sql`

---

### Caso 4: Pacientes con Diagnóstico Específico

**Pregunta clínica**: "¿Qué pacientes tienen diagnóstico de diabetes?"

**Tabla ancla**: MR_Diagnos

**Filtros clave**:
- `MRDIA_DiagnosCode LIKE 'E10%'` (Diabetes tipo 1)
- `MRDIA_DiagnosCode LIKE 'E11%'` (Diabetes tipo 2)

**Ver consulta completa**: `consultas/clinicas/diagnostico_especifico.sql`

---

### Caso 5: Lista de Espera Quirúrgica

**Pregunta clínica**: "¿Qué pacientes están esperando cirugía?"

**Tabla ancla**: WTL_* (Wait List)

**Filtros clave**:
- Estado activo de lista de espera

**Ver consulta completa**: `consultas/clinicas/lista_espera_quirurgica.sql`

---

## ✅ Validación de Consultas

Antes de ejecutar cualquier consulta, **SIEMPRE valídala** con el script de seguridad.

### Validación Manual (Checklist)

```
[ ] ¿Tiene TOP N? (máximo 1000)
[ ] ¿Es solo SELECT?
[ ] ¿No tiene UPDATE/DELETE/DROP?
[ ] ¿Tiene WHERE en tablas grandes?
[ ] ¿Está documentada?
[ ] ¿Tiene ORDER BY apropiado?
```

### Validación Automática (Python)

```bash
cd herramientas/python
python validador_consultas.py

# Validar un archivo SQL
>>> from validador_consultas import validate_sql_file
>>> result = validate_sql_file("../../consultas/mi_consulta.sql")
>>> print(result)
```

**Ejemplo de salida**:
```
✅ CONSULTA VÁLIDA - Puede ejecutarse de forma segura

==================================================================
ADVERTENCIAS (RECOMENDADO CORREGIR):
==================================================================
1. ⚠️ OPTIMIZACIÓN: Evita SELECT *. Especifica las columnas necesarias

==================================================================
SUGERENCIAS DE MEJORA:
==================================================================
1. 💡 Considera agregar ORDER BY para ordenar los resultados
```

---

## 🔧 Resolución de Problemas

### Problema 1: "Connection refused" al conectar a BD

**Causa**: No tienes acceso de red al servidor

**Solución**:
1. Verificar que estás en la red del hospital
2. Verificar credenciales en `credentials/alma_iris.txt`
3. Contactar soporte IT para verificar firewall

---

### Problema 2: "No rows returned"

**Causa**: La consulta está correcta pero no hay datos que cumplan los filtros

**Solución**:
1. Verificar los filtros WHERE
2. Probar sin filtros (con TOP 10)
3. Verificar que las tablas tienen datos

**Ejemplo**:
```sql
-- Primero, verifica que la tabla tiene datos
SELECT TOP 10 * FROM SQLUser.PA_Adm;

-- Luego, agrega filtros de uno en uno
SELECT TOP 10 * FROM SQLUser.PA_Adm
WHERE PAADM_Type = 'I';
```

---

### Problema 3: "Query timeout"

**Causa**: La consulta es muy lenta o sin límites

**Solución**:
1. Verificar que tiene TOP N
2. Agregar WHERE con fechas acotadas
3. Revisar que los JOINs son correctos

---

### Problema 4: "Column not found"

**Causa**: Nombre de columna incorrecto

**Solución**:
1. Verificar en documentación: `datos_alma/config/schema_map.json`
2. Buscar columna similar: `@mapeo_trakcare ¿Qué columnas tiene la tabla X?`
3. Consultar diccionario de datos

---

## 💡 Mejores Prácticas

### 1. Siempre Documenta

Cada consulta DEBE tener:
```sql
-- CONSULTA: [Nombre descriptivo]
-- PROPÓSITO: [Para qué sirve]
-- TABLAS: [Tablas usadas]
-- FECHA: [Fecha de creación]
-- AUTOR: [Tu nombre]
-- LÍMITE: TOP [N]
```

### 2. Usa Alias Descriptivos

**❌ Mal**:
```sql
SELECT t1.col1, t2.col2
FROM tabla1 t1
JOIN tabla2 t2 ON t1.id = t2.id
```

**✅ Bien**:
```sql
SELECT
    PA.PAADM_ADMNo AS NumeroEpisodio,
    P.PAPER_Name AS NombrePaciente
FROM PA_Adm AS PA
JOIN PA_Person AS P ON PA.PAADM_PAPMI_DR = P.PAPER_RowId
```

### 3. Filtra Siempre por Fecha

Para tablas grandes, **SIEMPRE** usa filtro de fecha:
```sql
WHERE PA.PAADM_AdmDate >= DATEADD(MONTH, -6, GETDATE())
```

### 4. Prueba con TOP 10 Primero

Antes de ejecutar con TOP 100 o más, prueba con:
```sql
SELECT TOP 10 ...
```

### 5. Guarda tus Consultas

Organiza tus consultas en carpetas:
```
consultas/
  ├── clinicas/
  │   ├── censo.sql
  │   ├── altas.sql
  │   └── diagnosticos.sql
  ├── administrativas/
  └── reportes/
```

### 6. Versiona tus Cambios

Usa nombres de archivo con versión:
```
censo_hospitalario_v1.sql
censo_hospitalario_v2_con_servicios.sql
```

### 7. Comparte con el Equipo

Cuando crees una consulta útil:
1. Documéntala completamente
2. Valídala con el script de seguridad
3. Compártela en el repositorio
4. Notifica al equipo

---

## 📞 Soporte

### Recursos de Ayuda

1. **Documentación Técnica**: `datos_alma/docs/`
2. **Ejemplos de Consultas**: `consultas/`
3. **Agentes de Claude Code**: `@mapeo_trakcare`, `@constructor_consultas`, etc.
4. **Validador de Consultas**: `herramientas/python/validador_consultas.py`

### Contacto

- **Soporte IT**: [contacto IT]
- **Equipo de Datos**: [contacto datos]
- **Documentación**: Este repositorio en `c:\_Consultas`

---

**Última actualización**: 2026-01-25
**Versión**: 1.0.0
